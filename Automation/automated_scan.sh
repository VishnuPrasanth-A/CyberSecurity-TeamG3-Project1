#!/bin/bash
# automated_scan.sh
target=$1

echo "[+] Starting Nmap scan..."
sudo nmap -sS -sV -O -A $target -oN nmap_report.txt

echo "[+] Running Nikto..."
nikto -h http://$target > nikto_report.txt

echo "[+] Running Enum4linux..."
enum4linux $target > smb_enum.txt

echo "[+] Scans completed. Output saved."

