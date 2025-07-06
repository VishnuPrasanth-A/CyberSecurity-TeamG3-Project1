# 🔐 CyberSecurity Team G-3 - Project 1

## 📝 Project Title  
**Enterprise-Level Basic Vulnerability Assessment of a Small Business Network**

---

## 📘 Overview  
This project simulates a basic vulnerability assessment and penetration testing scenario using industry-standard tools in a controlled lab environment.  
The objective is to identify misconfigurations and outdated services running on a vulnerable virtual machine (**Metasploitable2**) using an attacker machine (**Kali Linux**).

---

## 🧠 Objectives

- Setup a virtual penetration testing lab using VirtualBox  
- Automate enumeration and reconnaissance tasks  
- Identify vulnerable services and misconfigurations  
- Generate a detailed vulnerability assessment report in PDF format  

---

## 👥 Team Members

| Name               | Role                                 |
|--------------------|--------------------------------------|
| Vishnu Prasanth A  | Team Lead / Automation & Reporting   |
| Vivek Kumar        | Reconnaissance & SMB Enumeration     |
| Ashik              | Exploitation & Vulnerability Analysis|

---

## 🧪 Tools Used

- 🔧 **Kali Linux** – Penetration Testing OS  
- 🧱 **Metasploitable2** – Vulnerable target VM  
- 🛠️ **Nmap** – Network Mapper & OS detection  
- 🌐 **Nikto** – Web Server Vulnerability Scanner  
- 🔍 **Enum4linux** – SMB Enumeration Tool  
- 🐚 **Bash** – Automation Scripting  
- 🧾 **ReportLab (Python)** – PDF Report Generation

---

## 🚀 How to Run the Automation Script

1. Place both VMs in the same **Host-Only Network**
2. Boot **Metasploitable2** first, then **Kali Linux**
3. On Kali, give the script execute permission:


chmod +x automated_scan.sh
Run the script:

bash
Copy
Edit
sudo ./automated_scan.sh <target-ip>
This will generate the following output files:

nmap_report.txt

nikto_report.txt

smb_enum.txt

vulnerability_report.pdf ✅

🔍 Findings Summary
Vulnerability	Severity	Description
Anonymous FTP Access	High	vsftpd 2.3.4 allows anonymous login
Outdated Apache & PHP	High	Apache 2.2.8, PHP 5.2 vulnerable
Directory Indexing	Medium	Accessible /test/, /phpMyAdmin/
XST & TRACE Enabled	Medium	Allows Cross Site Tracing (XST) attacks
SSLv2 on SMTP	High	Insecure and deprecated SSL protocol

📄 Final Report
All findings, tool outputs, analysis, and screenshots are included in the PDF:
📎 Cybersecurity_Project_Report.pdf

📌 Note
This project was conducted strictly for educational purposes in a controlled lab environment.
Do not scan or attack real systems without explicit written permission.

🌟 Credits
Big thanks to all contributors for their research, scripting, and teamwork that made this project a success 🚀
– CyberSecurity Team G-3
