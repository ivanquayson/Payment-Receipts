from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


def get_receipt_details():
    details = {}

    def get_string(prompt):
        while True:
            value = input(prompt)
            if any(char.isdigit() for char in value):
                print("Invalid input: Input should not contain numbers. Please try again.")
            else:
                return value

    def get_number(prompt, number_type=int):
        while True:
            try:
                value = number_type(input(prompt))
                return value
            except ValueError:
                print(f"Invalid input: Please enter a valid {number_type.__name__}.")

    def getdate(prompt):
        from datetime import datetime
        while True:
            date_str = input(prompt)
            try:
                date = datetime.strptime(date_str, "%d-%m-%Y")
                return date_str
            except ValueError:
                print("Invalid date format: Please enter the date in DD-MM-YYYY format.")

    # Company details
    details["company_name"] = get_string("Enter company name: ")
    details["company_address"] = input("Enter company address: ")
    details["company_city"] = get_string("Enter company city: ")

    # Bill To details
    details["bill_to_name"] = get_string("Enter Bill To name: ")
    details["bill_to_address"] = input("Enter Bill To address: ")
    details["bill_to_city"] = get_string("Enter Bill To city: ")

    # Receipt details
    details["receipt_number"] = input("Enter receipt number: ")
    details["receipt_date"] = getdate("Enter receipt date (DD-MM-YYYY): ")

    # Items
    details["items"] = []
    while True:
        item = {}
        item["qty"] = input("Enter item quantity: ")
        item["description"] = input("Enter item description: ")
        item["unit_price"] = input("Enter item unit price: ")
        item["amount"] = input("Enter item amount: ")
        details["items"].append(item)
        more = input("Add another item? (yes/no): ")
        if more.lower() != "yes":
            break

    # Totals
    details["subtotal"] = input("Enter subtotal: ")
    details["sales_tax"] = input("Enter sales tax: ")
    details["total"] = input("Enter total: ")

    # Notes
    details["notes"] = input("Enter notes: ")

    return details


def generate_receipt(details, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()

    if 'Title' not in styles:
        styles.add(ParagraphStyle(name='Title', fontSize=18, leading=22, spaceAfter=12))

    if 'Heading' not in styles:
        styles.add(ParagraphStyle(name='Heading', fontSize=12, leading=14, spaceAfter=8))

    if 'Body' not in styles:
        styles.add(ParagraphStyle(name='Body', fontSize=10, leading=12, spaceAfter=6))

    # Company details
    company_info = f"""
    <b>{details["company_name"]}</b><br/>
    {details["company_address"]}<br/>
    {details["company_city"]}<br/>
    """
    elements.append(Paragraph(company_info, styles['Body']))

    # Spacer
    elements.append(Spacer(1, 70))

    # Bill To details
    bill_to_info = f"""
    <b>Billed To</b><br/>
    {details["bill_to_name"]}<br/>
    {details["bill_to_address"]}<br/>
    {details["bill_to_city"]}<br/>
    """
    elements.append(Paragraph(bill_to_info, styles['Body']))

    # Spacer
    elements.append(Spacer(1, 12))

    # Receipt details
    receipt_info = f"""
    <b>Receipt #</b> {details["receipt_number"]}<br/>
    <b>Receipt date</b> {details["receipt_date"]}<br/>
    """
    elements.append(Paragraph(receipt_info, styles['Body']))

    # Spacer
    elements.append(Spacer(1, 24))

    # Table of items
    table_data = [["QTY", "Description", "Unit Price", "Amount"]]
    for item in details["items"]:
        table_data.append([item["qty"], item["description"], item["unit_price"], item["amount"]])

    table = Table(table_data, colWidths=[0.5 * inch, 3 * inch, 1 * inch, 1 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#054D02')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),  # line under last item
    ]))
    elements.append(table)

    # Spacer
    elements.append(Spacer(1, 12))

    # Totals
    totals_table_data = [
        ["", "", "Subtotal", details["subtotal"]],
        ["", "", "Sales Tax (5%)", details["sales_tax"]],
        ["", "", "<b>Total (GH)</b>", f"<b>{details['total']}</b>"]
    ]
    totals_table = Table(totals_table_data, colWidths=[0.5 * inch, 3 * inch, 1 * inch, 1 * inch])
    totals_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LINEBELOW', (2, 1), (3, 1), 1, colors.black),  # line below sales tax
        ('LINEBELOW', (2, 2), (3, 2), 1, colors.black),  # line below total
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('FONTNAME', (2, -1), (3, -1), 'Helvetica-Bold'),
    ]))

    totals_table_style = TableStyle([
        ('ALIGN', (2, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (3, 0), (-1, -1), 'RIGHT'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('FONTNAME', (2, -1), (3, -1), 'Helvetica-Bold'),
        ('LINEBELOW', (2, 1), (3, 1), 1, colors.black),  # line below sales tax
        ('LINEBELOW', (2, 2), (3, 2), 1, colors.black),  # line below total
    ])
    totals_table.setStyle(totals_table_style)

    elements.append(totals_table)

    # Spacer
    elements.append(Spacer(1, 24))

    # Notes
    notes_info = f"""
    <b>Notes:</b><br/>
    {details["notes"]}<br/>
    """
    elements.append(Paragraph(notes_info, styles['Body']))

    # Build PDF
    doc.build(elements)


# Get receipt details from user input
details = get_receipt_details()

# Define output path
output_path = "generated_receipt.pdf"  # Update this path to the desired output location

# Generate the receipt
generate_receipt(details, output_path)

print("Receipt generated successfully!")