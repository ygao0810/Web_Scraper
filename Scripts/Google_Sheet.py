import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets API credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\32309\Desktop\Hasmo Project\myenv1\Data\Raw\downloaded_html\web-scraper-development-1ca92a8a6b0d.json", scope)
client = gspread.authorize(creds)

# Create or open a Google Sheet
sheet = client.create("Hasmo Market Research Data")
worksheet = sheet.sheet1

# Add data to Google Sheets
worksheet.update('A1', 'Service Offerings')
worksheet.update('A2', [[service] for service in service_offerings])

worksheet.update('B1', 'Case Studies')
worksheet.update('B2', [[case] for case in case_studies])

worksheet.update('C1', 'Client Testimonials')
worksheet.update('C2', [[testimonial] for testimonial in client_testimonials])

worksheet.update('D1', 'Thought Leadership')
worksheet.update('D2', [[article] for article in thought_leadership])

worksheet.update('E1', 'Market Insights')
worksheet.update('E2', [[insight] for insight in market_insights])