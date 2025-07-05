🔐 CyberSecurity Team G-3 - Project 1

📝 Project Title:

Enterprise-Level Basic Vulnerability Assessment of a Small Business Network

📘 Overview

This project simulates a basic vulnerability assessment and penetration testing scenario using industry-standard tools in a controlled lab environment. The goal is to identify misconfigurations and outdated services running on a vulnerable virtual machine (Metasploitable2) using an attacker machine (Kali Linux).

🧠 Objectives

Setup a virtual penetration testing lab using VirtualBox

Automate enumeration and reconnaissance tasks

Identify vulnerable services and misconfigurations

Generate a detailed vulnerability assessment report

👥 Team Members

Name

Role

Vishnu Prasanth A

Team Lead / Automation & Reporting

Member A

Reconnaissance & SMB Enumeration

Member B

Exploitation & Vulnerability Analysis

🧪 Tools Used

🔧 Kali Linux – Penetration Testing OS

🧱 Metasploitable2 – Vulnerable target VM

🛠️ Nmap – Network Mapper & OS detection

🌐 Nikto – Web server vulnerability scanner

🔍 Enum4linux – SMB Enumeration tool

💻 Bash – Automation scripting

🚀 How to Run the Automation Script

Place both VMs in the same Host-Only Network

Boot Metasploitable2 first, then Kali Linux

On Kali, make the script executable:

chmod +x automated_scan.sh

Run the script:

sudo ./automated_scan.sh <target-ip>

Outputs will be saved in:

nmap_report.txt

nikto_report.txt

smb_enum.txt

📁 Repository Structure

CyberSecurity-TeamG3-Project1/
├── automated_scan.sh
├── nmap_report.txt
├── nikto_report.txt
├── smb_enum.txt
├── Cybersecurity_Project_Report.pdf
├── /screenshots/
│   ├── ping from kali to met.png
│   ├── port analysis.png
│   └── ...
└── README.md

🔍 Findings Summary

Vulnerability

Severity

Description

Anonymous FTP Access

High

vsftpd 2.3.4 allows anonymous login

Outdated Apache & PHP Versions

High

Apache 2.2.8, PHP 5.2 vulnerable

Directory Indexing Enabled

Medium

Accessible /test/, /phpMyAdmin/

XST & TRACE Enabled

Medium

Allows XST attacks

SSLv2 Supported on SMTP

High

Insecure and deprecated SSL protocol

📄 Final Report

All findings, tools used, screenshots, and team contributions are documented in the full PDF report:

📎 Cybersecurity_Project_Report.pdf

📌 Note

This project was conducted strictly for educational purposes in a controlled lab environment. Do not scan or attack real systems without explicit written permission.

🌟 Credits

Thanks to all contributors for active participation, research, and collaboration in CyberSecurity Team G-3.
