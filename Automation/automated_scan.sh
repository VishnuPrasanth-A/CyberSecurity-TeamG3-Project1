#!/bin/bash
# automated_scan.sh

target=$1

if [ -z "$target" ]; then
  echo "Usage: $0 <target-ip-or-domain>"
  exit 1
fi

echo "[+] Starting Nmap scan..."
sudo nmap -sS -sV -O -A "$target" -oN nmap_report.txt

echo "[+] Running Nikto..."
nikto -h "http://$target" > nikto_report.txt

echo "[+] Running Enum4linux..."
enum4linux "$target" > smb_enum.txt

echo "[+] Scans completed. Output saved."

echo "[+] Generating PDF report..."
python3 report_gen.py

echo "[+] Report generated: vulnerability_report.pdf"
