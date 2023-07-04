# Pyports is a port-scanning and web-scraping tool written in python

A simple Python tool for scanning WordPress websites for open ports and finding common WordPress paths.

## Installation

1. Make sure Python is installed on your system (version 3.6 or higher).
2. Clone the repository or download the files.
3. Navigate to the project directory.

4. Install the required libraries using the following command:

pip install -r requirements.txt

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the script using the following command:

python wordpress_scan.py -t [target-domain]

Replace `[target-domain]` with the WordPress domain you want to scan.
3. The script will perform a port scan and display the status of the scanned ports.
4. After that, it will search for common WordPress paths and display them.

## Options

- `-t`, `--target`: The target domain of the WordPress website (required).
- `-p`, `--ports`: A list of ports for the port scan (default: 21, 22, 80, 443, 445, 993, 995, 3306, 3389, 8443, 8080).
- `-v`, `--verbose`: Enable verbose mode to display closed ports as well.

## Example

python wordpress_scan.py -t example.com

## Notes

- Use this tool responsibly and only with the consent of the owner of the target website.
- Check applicable laws and regulations in your region before using the tool.

## Authors

This project was developed by Maik Jeschke. Contact me at maik.jeschke0101[at]gmail.com for any questions or feedback.


# Pyports is a port-scanning and web-scraping tool written in python

Ein einfaches Python-Tool zum Scannen von WordPress-Websites auf offene Ports und zum Auffinden gängiger WordPress-Pfade.

## Installation

1. Stellen Sie sicher, dass Python auf Ihrem System installiert ist (Version 3.6 oder höher).
2. Klone Sie das Repository oder laden Sie die Dateien herunter.
3. Navigieren Sie zum Verzeichnis des Projekts.

4. Installieren Sie die erforderlichen Bibliotheken mit dem Befehl:

pip install -r requirements.txt

## Verwendung

1. Öffnen Sie ein Terminal oder eine Befehlszeile und navigieren Sie zum Verzeichnis des Projekts.
2. Führen Sie das Skript mit dem folgenden Befehl aus:

python wordpress_scan.py -t [Ziel-Host o. Domain]

Ersetzen Sie `[Ziel-Domain]` durch die zu scannende WordPress-Domain.
3. Das Skript führt einen Port-Scan durch und gibt den Status der gescannten Ports aus.
4. Anschließend sucht das Skript nach gängigen WordPress-Pfaden und gibt sie aus.

## Optionen

- `-t`, `--target`: Die Ziel-Domain der WordPress-Website (erforderlich).
- `-p`, `--ports`: Eine Liste von Ports für den Port-Scan (Standard: 21, 22, 80, 443, 445, 993, 995, 3306, 3389, 8443, 8080).
- `-v`, `--verbose`: Aktiviert den ausführlichen Modus, der auch geschlossene Ports anzeigt.

## Beispiel

## Hinweise

- Verwenden Sie dieses Tool verantwortungsvoll und nur mit Zustimmung des Eigentümers der Ziel-Website.
- Überprüfen Sie die geltenden Gesetze und Richtlinien in Ihrer Region, bevor Sie das Tool verwenden.

## Autoren

Dieses Projekt wurde von Maik Jeschke entwickelt. Kontaktieren Sie mich unter maik.jeschke0101[at]gmail.com für Fragen oder Feedback.





