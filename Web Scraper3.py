from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning
import warnings
import requests
import scrapy
import gspread
import csv
import openai

# Suppress BS4 URL warnings
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

# Target URL and headers
url = "https://www.mycwt.com/"
headers = {'User-Agent': 'Mozilla/5.0 (compatible; FrenchwayBot/1.0)'}
response = requests.get(url, headers=headers)

# Fetch HTML
if response.status_code == 200:
    html = response.text
    print(f"Fetched {len(html)} characters from {url}")

    # Save raw HTML
    output_path = r"C:\Users\32309\Desktop\Hasmo Project\myenv1\Data\Raw\downloaded_html\page.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved raw HTML to {output_path}")
else:
    print(f"Failed to fetch {url}: {response.status_code}")
    html = ''

# Parse HTML content
soup = BeautifulSoup(html, 'html.parser')

data = {
    "service_offerings": [],
    "case_studies": [],
    "client_testimonials": [],
    "thought_leadership": [],
    "market_insights": []
}

# Extract service offerings
for service in soup.find_all('div', class_='service-title'):
    data['service_offerings'].append(service.get_text(strip=True))

# Extract case studies
for case in soup.find_all('div', class_='case-study-title'):
    data['case_studies'].append(case.get_text(strip=True))

# Extract client testimonials
for testimonial in soup.find_all('blockquote'):
    data['client_testimonials'].append(testimonial.get_text(strip=True))

# Extract thought leadership articles
for article in soup.find_all('div', class_='thought-leadership-title'):
    data['thought_leadership'].append(article.get_text(strip=True))

# Extract market insights
for insight in soup.find_all('div', class_='market-insight-title'):
    data['market_insights'].append(insight.get_text(strip=True))

# Print structured data
for key, items in data.items():
    print(f"{key}: {items}")

# Write data to CSV
csv_file = 'market_research_data.csv'
fieldnames = list(data.keys())
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    max_len = max(len(data[field]) for field in fieldnames)
    for i in range(max_len):
        row = {field: data[field][i] if i < len(data[field]) else '' for field in fieldnames}
        writer.writerow(row)
print(f"Data written to {csv_file}")


# Sample HTML content
url = """
<html>
<head><title>Example Page</title></head>
<body>
    <h1>Main Title</h1>
    <div class="service-title">Service 1</div>
    <div class="service-title">Service 2</div>
    <h2>Case Study</h2>
    <p>This is a case study.</p>
    <blockquote class="testimonial">Client testimonial text.</blockquote>
    <h2>Thought Leadership</h2>
    <a href="#">Thought leadership article</a>
    <h2>Market Insight</h2>
    <p>Insight text.</p>
</body>
</html>
"""

# Parse the HTML content
soup = BeautifulSoup(url, 'html.parser')

case_study_title = soup.find('h2').get_text()
case_study_text = soup.find('p').get_text()

print(case_study_title)  # Output: Case Study
print(case_study_text)   # Output: This is a case study.




# Set up OpenAI API key
openai.api_key = ''

# Example function to analyze market insights
def analyze_market_insights(insights):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following market insights and summarize key trends:\n{insights}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Analyze extracted market insights
market_insights_text = " ".join(market_insights)
analysis = analyze_market_insights(market_insights_text)
print(analysis)


# Scrapy spider remains unchanged
class ServicesSpider(scrapy.Spider):
    name = "services"
    start_urls = [url]

    def parse(self, response):
        for service in response.css("div.service-title"):
            yield {
                "title": service.css("h3::text").get(),
                "description": service.css("p::text").get()
            }

        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
