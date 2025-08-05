import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets API credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name("", scope)
client = gspread.authorize(creds)

#AmexGBT

# Create or open a Google Sheet
sheet1 = client.create("AmexGBT")

# Add data to Google Sheets
sheet1.update('A1', 'Service Offerings')
sheet1.update('A2', [[service] for service in service_offerings])

sheet1.update('B1', 'Case Studies')
sheet1.update('B2', [[case] for case in case_studies])

sheet1.update('C1', 'Client Testimonials')
sheet1.update('C2', [[testimonial] for testimonial in client_testimonials])

sheet1.update('D1', 'Thought Leadership')
sheet1.update('D2', [[article] for article in thought_leadership])

sheet1.update('E1', 'Market Insights')
sheet1.update('E2', [[insight] for insight in market_insights])

#mycwt

# Create or open a Google Sheet
sheet2 = client.create("mycwt")

# Add data to Google Sheets
sheet2.update('A1', 'Service Offerings')
sheet2.update('A2', [[service] for service in service_offerings])

sheet2.update('B1', 'Case Studies')
sheet2.update('B2', [[case] for case in case_studies])

sheet2.update('C1', 'Client Testimonials')
sheet2.update('C2', [[testimonial] for testimonial in client_testimonials])

sheet2.update('D1', 'Thought Leadership')
sheet2.update('D2', [[article] for article in thought_leadership])

sheet2.update('E1', 'Market Insights')
sheet2.update('E2', [[insight] for insight in market_insights])

#bcdtravel

# Create or open a Google Sheet
sheet3 = client.create("bcdtravel")

# Add data to Google Sheets
sheet3.update('A1', 'Service Offerings')
sheet3.update('A2', [[service] for service in service_offerings])

sheet3.update('B1', 'Case Studies')
sheet3.update('B2', [[case] for case in case_studies])

sheet3.update('C1', 'Client Testimonials')
sheet3.update('C2', [[testimonial] for testimonial in client_testimonials])

sheet3.update('D1', 'Thought Leadership')
sheet3.update('D2', [[article] for article in thought_leadership])

sheet3.update('E1', 'Market Insights')
sheet3.update('E2', [[insight] for insight in market_insights])

#tzell

# Create or open a Google Sheet
sheet4 = client.create("tzell")

# Add data to Google Sheets
sheet4.update('A1', 'Service Offerings')
sheet4.update('A2', [[service] for service in service_offerings])

sheet4.update('B1', 'Case Studies')
sheet4.update('B2', [[case] for case in case_studies])

sheet4.update('C1', 'Client Testimonials')
sheet4.update('C2', [[testimonial] for testimonial in client_testimonials])

sheet4.update('D1', 'Thought Leadership')
sheet4.update('D2', [[article] for article in thought_leadership])

sheet4.update('E1', 'Market Insights')
sheet4.update('E2', [[insight] for insight in market_insights])

#egencia

# Create or open a Google Sheet
sheet5 = client.create("egencia")

# Add data to Google Sheets
sheet5.update('A1', 'Service Offerings')
sheet5.update('A2', [[service] for service in service_offerings])

sheet5.update('B1', 'Case Studies')
sheet5.update('B2', [[case] for case in case_studies])

sheet5.update('C1', 'Client Testimonials')
sheet5.update('C2', [[testimonial] for testimonial in client_testimonials])

sheet5.update('D1', 'Thought Leadership')
sheet5.update('D2', [[article] for article in thought_leadership])

sheet5.update('E1', 'Market Insights')
sheet5.update('E2', [[insight] for insight in market_insights])

#travelperk

# Create or open a Google Sheet
sheet6 = client.create("travelperk")

# Add data to Google Sheets
sheet6.update('A1', 'Service Offerings')
sheet6.update('A2', [[service] for service in service_offerings])

sheet6.update('B1', 'Case Studies')
sheet6.update('B2', [[case] for case in case_studies])

sheet6.update('C1', 'Client Testimonials')
sheet6.update('C2', [[testimonial] for testimonial in client_testimonials])

sheet6.update('D1', 'Thought Leadership')
sheet6.update('D2', [[article] for article in thought_leadership])

sheet6.update('E1', 'Market Insights')
sheet6.update('E2', [[insight] for insight in market_insights])

#FCM Travel Solutions

#Direct Travel

#Navan (formerly TripActions)

#Le Connoisseur

#BlueOrange Travel – Fashion Division

#Luxe Fashion Trips

#Forest Travel

#Académie des Arts de Vivre

#Exclusive France Tours

#Deluxe France

#French Promise