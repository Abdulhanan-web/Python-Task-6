from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generate_pdf(data, report_type="Student"):
    if not data:
        print("No data available!")
        return

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{report_type}_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph(f"{report_type} Report", styles['Title']))
    elements.append(Spacer(1, 10))

    # Date
    elements.append(Paragraph(f"Generated on: {datetime.now()}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Table Data
    table_data = [["Name", "ID", "Email", "Role", "Performance"]]

    for item in data:
        table_data.append([
            item.get("name", ""),
            item.get("id", ""),
            item.get("email", ""),
            item.get("role", ""),
            item.get("performance", "")
        ])

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    elements.append(table)

    doc.build(elements)

    print(f"PDF generated successfully: {filename}")