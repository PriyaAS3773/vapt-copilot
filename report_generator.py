import json
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_pdf_report(json_file, ai_analysis_file, output_pdf="VAPT_Report.pdf"):
    with open(json_file, 'r') as f:
        scan_data = json.load(f)

    with open(ai_analysis_file, 'r', encoding='utf-8') as f:
        ai_text = f.read()

    doc = SimpleDocTemplate(output_pdf, pagesize=A4,
                             topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Title'],
        fontSize=22, textColor=colors.HexColor("#1a237e"), spaceAfter=10
    )
    heading_style = ParagraphStyle(
        'HeadingStyle', parent=styles['Heading2'],
        fontSize=14, textColor=colors.HexColor("#0d47a1"),
        spaceBefore=16, spaceAfter=8
    )
    normal_style = styles['Normal']

    elements = []

    elements.append(Paragraph("VAPT Security Report", title_style))
    elements.append(Paragraph(f"Target: {scan_data['target']}", normal_style))
    elements.append(Paragraph(f"Scan Time: {scan_data['scan_time']}", normal_style))
    elements.append(Paragraph(
        f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        normal_style
    ))
    elements.append(Spacer(1, 20))

    for host in scan_data["hosts"]:
        elements.append(Paragraph(f"Host: {host['ip']} ({host['hostname']})", heading_style))
        elements.append(Paragraph(f"State: {host['state']}", normal_style))
        elements.append(Spacer(1, 8))

        for proto, ports in host["protocols"].items():
            elements.append(Paragraph(f"Protocol: {proto.upper()}", heading_style))

            table_data = [["Port", "State", "Service", "Product", "Version"]]
            for p in ports:
                table_data.append([
                    str(p["port"]), p["state"], p["service"],
                    p.get("product", "-") or "-",
                    p.get("version", "-") or "-"
                ])

            table = Table(table_data, colWidths=[2.5*cm, 2.5*cm, 3*cm, 4*cm, 4*cm])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1a237e")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            elements.append(table)
            elements.append(Spacer(1, 15))

    elements.append(PageBreak())
    elements.append(Paragraph("AI Security Analysis", title_style))
    elements.append(Spacer(1, 10))

    for line in ai_text.split("\n"):
        line = line.strip()
        if not line:
            elements.append(Spacer(1, 6))
            continue
        if line.startswith("#") or line.isupper():
            elements.append(Paragraph(line.replace("#", "").strip(), heading_style))
        else:
            elements.append(Paragraph(line, normal_style))

    doc.build(elements)
    print(f"\n[+] PDF report generated: {output_pdf}")


if __name__ == "__main__":
    json_file = input("Enter JSON scan file name: ")
    ai_file = input("Enter AI analysis text file name: ")

    generate_pdf_report(json_file, ai_file)