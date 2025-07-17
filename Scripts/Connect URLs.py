import requests

url = "https://www.mycwt.com/"
headers = {'User-Agent': 'Mozilla/5.0 (compatible; FrenchwayBot/1.0)'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Store HTML in a variable
    html = response.text
    print(f"Fetched {len(html)} characters from {url}")

    # Save the raw HTML to the specified Windows directory
    output_path = r"C:\Users\32309\Desktop\Hasmo Project\myenv1\Data\Raw\downloaded_html\page.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved raw HTML to {output_path}")
else:
    print(f"Failed to fetch {url}: {response.status_code}")
