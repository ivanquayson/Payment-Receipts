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
    details["company_city"] = input("Enter company city and state: ")

    # Bill To details
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


def generate_receipt(details, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []

