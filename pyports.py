import socket
import argparse
import concurrent.futures
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Definieren der gängigen Pfade in WordPress
common_paths = ['/wp-admin/', '/wp-login.php', '/htdocs', '/wp-content/themes', '/wp-content/plugins', '/wp-content/uploads']

def print_banner(banner):
    print(banner)

def check_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
    return port, result == 0

def port_scan(target, ports, verbose):
    open_ports = []
    closed_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_port = {executor.submit(check_port, target, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                _, is_open = future.result()
                if is_open:
                    open_ports.append(port)
                else:
                    closed_ports.append(port)
                if verbose:
                    print(f"Port {port} is {'open' if is_open else 'closed'}")
            except Exception as exc:
                print(f"Port {port} generated an exception: {exc}")

    with open('port_results.txt', 'w') as file:
        file.write('Open Ports:\n')
        for port in open_ports:
            file.write(f'Port {port} is open\n')
        file.write('\nClosed Ports:\n')
        for port in closed_ports:
            file.write(f'Port {port} is closed\n')

    print("\nPort scan results:")
    print(f"Open Ports: {open_ports}")
    print(f"Closed Ports: {closed_ports}")

def find_paths(target):
    response = requests.get(f"http://{target}")
    soup = BeautifulSoup(response.text, 'html.parser')
    found_paths = []

    for link in soup.find_all('a'):
        url = urljoin(response.url, link.get('href'))

        for path in common_paths:
            if path in url:
                found_paths.append(url)
                break

    with open('path_results.txt', 'w') as file:
        file.write('Found paths:\n')
        for path in found_paths:
            file.write(f'{path}\n')

    print("\nPath scan results:")
    for path in found_paths:
        print(path)

def main():
    parser = argparse.ArgumentParser(description='Port Scan and Web Scraper Tool.')
    parser.add_argument('-t', '--target', type=str, required=True, help='Target domain')
    parser.add_argument('-p', '--ports', type=int, nargs='+',
                        default=[21, 22, 80, 443, 445, 993, 995, 3306, 3389, 8443, 8080],
                        help='Ports for the port scan')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')

    args = parser.parse_args()

    banner = """
   __ __         __     __  __        ___  __             __    __
  / // ___ _____/ /__  / /_/ / ___   / _ \/ ___ ____ ___ / /_  / /
 / _  / _ `/ __/  '_/ / __/ _ / -_) / ___/ / _ `/ _ / -_/ __/ /_/
/_//_/\_,_/\__/_/\_\  \__/_//_\__/ /_/  /_/\_,_/_//_\__/\__/ (_)
    """
    print_banner(banner)

    print("\nScanning ports, please wait...")
    port_scan(args.target, args.ports, args.verbose)
    print("Port scan results saved in port_results.txt")

    print("\nLooking for common WordPress paths...")
    find_paths(args.target)
    print("Path scan results saved in path_results.txt")

if __name__ == '__main__':
    main()
