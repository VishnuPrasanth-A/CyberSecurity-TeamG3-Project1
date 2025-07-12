# 🧱 Victim Machine: Metasploitable2

## 💡 What is Metasploitable2?

Metasploitable2 is a purposefully vulnerable Linux virtual machine created by Rapid7. It is widely used for learning, practicing, and testing penetration testing skills in a safe lab environment.

- OS: Ubuntu 8.04 Server (outdated and vulnerable)
- Default login:  
  - Username: `msfadmin`  
  - Password: `msfadmin`

---

## 🧪 Key Vulnerable Services Pre-installed:

| Port | Service           | Notes                              |
|------|-------------------|-------------------------------------|
| 21   | vsftpd            | Allows anonymous login              |
| 22   | SSH               | Outdated version                    |
| 23   | Telnet            | Unencrypted login                   |
| 80   | Apache HTTPD      | Runs outdated web apps              |
| 139  | SMB               | SAMBA file sharing enabled          |
| 3306 | MySQL             | Weak/default credentials possible   |

---

## ⚙️ How to Setup (Quick Steps):

1. **Download Metasploitable2** from [Rapid7 download link](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)
2. Import into **VirtualBox** or **VMware**
3. Set the network mode to **Host-Only Adapter** (or the same network as Kali)
4. Start the VM — login using:
   ```bash
   Username: msfadmin
   Password: msfadmin
