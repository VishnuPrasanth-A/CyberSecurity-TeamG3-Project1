from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import re
import os

# ------------ Parse Report Files ------------

def parse_nmap(filename):
    risks = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            for line in content.splitlines():
                if re.search(r'open', line) and re.search(r'\d+/tcp', line):
                    port = re.search(r'(\d+/tcp)\s+open', line)
                    service = re.search(r'\d+/tcp\s+open\s+([\w\-]+)', line)
                    if port and service:
                        service_name = service.group(1).lower()
                        level = 'Low'
                        if 'ftp' in service_name or 'telnet' in service_name:
                            level = 'High'
                        elif 'http' in service_name or 'smtp' in service_name:
                            level = 'Medium'
                        risks.append((f"Nmap found {service_name} on {port.group(1)}", level))
    except Exception as e:
        print(f"[!] Error reading {filename}: {e}")
    return risks

def parse_nikto(filename):
    risks = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if "OSVDB" in line or "X-" in line or "vulnerable" in line.lower():
                    level = "High" if "vulnerable" in line.lower() else "Medium"
                    risks.append((f"Nikto: {line.strip()}", level))
    except Exception as e:
        print(f"[!] Error reading {filename}: {e}")
    return risks

def parse_enum4linux(filename):
    risks = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if "password" in line.lower() or "anonymous" in line.lower():
                    level = "High" if "no password" in line.lower() else "Medium"
                    risks.append((f"Enum4linux: {line.strip()}", level))
    except Exception as e:
        print(f"[!] Error reading {filename}: {e}")
    return risks

# ------------ Suggested Resolution ------------

def get_resolution(risk_text):
    risk_text = risk_text.lower()
    if 'ftp' in risk_text:
        return 'Disable FTP or use secure SFTP with authentication.'
    elif 'telnet' in risk_text:
        return 'Disable Telnet; use SSH instead.'
    elif 'http' in risk_text:
        return 'Use HTTPS and update web server software.'
    elif 'smtp' in risk_text:
        return 'Apply spam filters and enable authentication.'
    elif 'anonymous' in risk_text or 'smb' in risk_text:
        return 'Restrict SMB access and disable anonymous login.'
    elif 'outdated' in risk_text or 'osvdb' in risk_text:
        return 'Update the vulnerable software/service.'
    elif 'password' in risk_text:
        return 'Enforce strong password policies.'
    else:
        return 'Review and secure this service.'

# ------------ Generate Table-Based PDF ------------

def generate_pdf_table(findings, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>Vulnerability Assessment Report</b>", styles['Title']))
    elements.append(Spacer(1, 20))

    # Table header
    data = [["Vulnerability", "Risk Level", "Recommended Resolution"]]

    # Table body
    for finding, level in findings:
        resolution = get_resolution(finding)
        risk_color = {
            "High": colors.red,
            "Medium": colors.orange,
            "Low": colors.green
        }.get(level, colors.black)

        data.append([
            Paragraph(finding, styles['Normal']),
            Paragraph(f'<font color="{risk_color}"><b>{level}</b></font>', styles['Normal']),
            Paragraph(resolution, styles['Normal'])
        ])

    # Build the table
    table = Table(data, colWidths=[200, 100, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 0), (-1, -1), 0.25, colors.grey),
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.grey),
    ]))

    elements.append(table)
    doc.build(elements)
    print(f"[+] PDF report generated: {output_file}")

# ------------ Main Execution ------------

if __name__ == "__main__":
    findings = []

    # Get the absolute path of the current script directory.
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define file names with absolute paths.
    nmap_file = os.path.join(script_dir, "nmap_report.txt")
    nikto_file = os.path.join(script_dir, "nikto_report.txt")
    enum_file = os.path.join(script_dir, "smb_enum.txt")

    # Parse files if they exist; otherwise, notify and skip.
    if os.path.exists(nmap_file):
        findings += parse_nmap(nmap_file)
    else:
        print(f"[!] File not found: {nmap_file}")

    if os.path.exists(nikto_file):
        findings += parse_nikto(nikto_file)
    else:
        print(f"[!] File not found: {nikto_file}")

    if os.path.exists(enum_file):
        findings += parse_enum4linux(enum_file)
    else:
        print(f"[!] File not found: {enum_file}")

    # Only generate report if there are findings.
    if findings:
        output_pdf = os.path.join(script_dir, "vulnerability_report.pdf")
        generate_pdf_table(findings, output_pdf)
    else:
        print("[!] No findings to generate report.")
