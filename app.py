from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


def get_receipt_details():
    details = {}

    # Company details
    details["company_name"] = input("Enter company name: ")
    details["company_address"] = input("Enter company address: ")
    details["company_city"] = input("Enter company city: ")

    # Bill To details
    details["bill_to_name"] = input("Enter Bill To name: ")
    details["bill_to_address"] = input("Enter Bill To address: ")
    details["bill_to_city"] = input("Enter Bill To city: ")

    # Receipt details
    details["receipt_number"] = input("Enter receipt number: ")
    details["receipt_date"] = input("Enter receipt date (DD-MM-YYYY): ")

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
    else:
        styles['Title'].fontSize = 18
        styles['Title'].leading = 22
        styles['Title'].spaceAfter = 12

    if 'Heading' not in styles:
        styles.add(ParagraphStyle(name='Heading', fontSize=12, leading=14, spaceAfter=8))
    else:
        styles['Heading'].fontSize = 12
        styles['Heading'].leading = 14
        styles['Heading'].spaceAfter = 8

    if 'Body' not in styles:
        styles.add(ParagraphStyle(name='Body', fontSize=10, leading=12, spaceAfter=6))
    else:
        styles['Body'].fontSize = 10
        styles['Body'].leading = 12
        styles['Body'].spaceAfter = 6

    # Company details
    company_info = f"""
    <b>{details["company_name"]}</b><br/>
    {details["company_address"]}<br/>
    {details["company_city"]}<br/>
    """
    elements.append(Paragraph(company_info, styles['Body']))

    # Spacer
    elements.append(Spacer(1, 12))

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

