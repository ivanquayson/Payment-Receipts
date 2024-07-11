# Importing modules
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Data to be displayed as tables
data = [
    ["Date", "Name", "Subscription", "Price($)"],
    [
        "1/7/2024",
        "Python and Django Development Course",
        "1 year",
        "400/-"
    ],
    ["1/7/2024", "Udemy Classes: Live Session", "3 months", "275/-"],
    ["Sub Total", "", "", "675/-"],
    ["Discount", "", "", "50/-"],
    ["Total", "", "", "625/-"],
]

pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )

styles = getSampleStyleSheet() 