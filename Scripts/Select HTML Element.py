from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
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
soup = BeautifulSoup(html_content, 'html.parser')

case_study_title = soup.find('h2').get_text()
case_study_text = soup.find('p').get_text()

print(case_study_title)  # Output: Case Study
print(case_study_text)   # Output: This is a case study.