"""
get_receipts_details

Inputs
User inputs for company name, address, city, bill-to name, address, city, receipt number,
date, item details (quantity, description, unit price, amount), subtotal, sales tax,
total, and notes.

Flow
Initialize an empty dictionary details.
Collect company details and store them in the dictionary.
Collect bill-to details and store them in the dictionary.
Collect receipt details and store them in the dictionary.
Collect item details in a loop until the user decides to stop, and store them in a list within
the dictionary.
Collect subtotal, sales tax, and total, and store them in the dictionary.
Collect any additional notes and store them in the dictionary.
Return the populated details dictionary.

Outputs
A dictionary containing all the collected receipt details.
"""

# Importing modules
from PIL import Image
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def get_receipts_details():
    details = {}

    # Company details
    details["company_name"] = input("Enter company name: ")
    details["company_address"] = input("Enter company address: ")
    details["company_city"] = input("Enter company city and state: ")

    # Bill-to details
    details["bill_to_name"] = input("Enter Bill To name: ")
    details["bill_to_address"] = input("Enter Bill To address: ")
    details["bill_to_city"] = input("Enter Bill To city and state: ")

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


def generate_receipt(details, template_path, output_path):
    template = Image.open(template_path)
    template_width, template_height = template.size

    template_width_inch = template_width/300
    template_height_inch = template_height/300

    c = canvas.Canvas(output_path, pagesize=(template_width_inch * inch,
                                             template_height_inch * inch))
    c.drawImage(template_path, 0, 0, width=template_width_inch * inch,
                height=template_height_inch * inch)
    c.setFont("Helvetica", 10)