from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import re

# ------------ Parse Report Files ------------

def parse_nmap(filename):
    risks = []
    with open(filename, 'r') as f:
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
    return risks

def parse_nikto(filename):
    risks = []
    with open(filename, 'r') as f:
        for line in f:
            if "OSVDB" in line or "X-" in line or "vulnerable" in line.lower():
                level = "High" if "vulnerable" in line.lower() else "Medium"
                risks.append((f"Nikto: {line.strip()}", level))
    return risks

def parse_enum4linux(filename):
    risks = []
    with open(filename, 'r') as f:
        for line in f:
            if "password" in line.lower() or "anonymous" in line.lower():
                level = "High" if "no password" in line.lower() else "Medium"
                risks.append((f"Enum4linux: {line.strip()}", level))
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
            Paragraph(f'<font color="{risk_color.hexval()}"><b>{level}</b></font>', styles['Normal']),
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
    findings += parse_nmap("nmap_report.txt")
    findings += parse_nikto("nikto_report.txt")
    findings += parse_enum4linux("smb_enum.txt")

    generate_pdf_table(findings, "vulnerability_report.pdf")
