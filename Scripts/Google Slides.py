from googleapiclient.discovery import build
from google.oauth2 import service_account

# Setup Google Slides API credentials
creds = service_account.Credentials.from_service_account_file(r"C:\Users\32309\Desktop\Hasmo Project\myenv1\Data\Raw\downloaded_html\web-scraper-development-1ca92a8a6b0d.json")
service = build('slides', 'v1', credentials=creds)

# Create a new presentation
presentation = service.presentations().create(body={
    'title': 'Market Research Presentation'
}).execute()
presentation_id = presentation['presentationId']

# Add slides and content (example)
slides = service.presentations().batchUpdate(presentationId=presentation_id, body={
    'requests': [
        {
            'createSlide': {
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE_AND_TWO_COLUMNS'
                }
            }
        }
    ]
}).execute()