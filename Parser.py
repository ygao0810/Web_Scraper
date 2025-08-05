import requests
from bs4 import BeautifulSoup
from Competitor_Webs import COMPETITORS

data = {
    "service_offerings": [],
    "case_studies": [],
    "client_testimonials": [],
    "thought_leadership": [],
    "market_insights": []
}

# Track which competitors have been processed
processed = []

#Amex GBT

url1 = COMPETITORS.get("AmexGBT")
if url1:
    processed.append("AmexGBT")
    print(f"Fetching AmexGBT at {url1}")
    try:
        response1 = requests.get(url1)
        soup1 = BeautifulSoup(response1.text, 'html.parser')

        services_section1 = soup1.find_all('h2', class_='service-title')
        for service in services_section1:
            data['service_offerings'].append(service.get_text().strip())

        services_section1 = soup1.find_all('h2', class_='our-services')
        for service in services_section1:
            data['service_offerings'].append(service.get_text().strip())

        services_section1 = soup1.find_all('h2', class_='solutions')
        for service in services_section1:
            data['service_offerings'].append(service.get_text().strip())

        services_section1 = soup1.find_all('h2', class_='what-We-offer')
        for service in services_section1:
            data['service_offerings'].append(service.get_text().strip())

        case_studies_section1 = soup1.find_all('h2', class_='case-study-title')
        for case in case_studies_section1:
            data['case_studies'].append(case.get_text().strip())

        testimonials_section1 = soup1.find_all('blockquote')
        for testimonial in testimonials_section1:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section1 = soup1.find_all('Clients')
        for testimonial in testimonials_section1:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section1 = soup1.find_all('our-work')
        for testimonial in testimonials_section1:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section1 = soup1.find_all('success-stories')
        for testimonial in testimonials_section1:
            data['client_testimonials'].append(testimonial.get_text().strip())

        thought_leadership_section1 = soup1.find_all('h2', class_='thought-leadership-title')
        for article in thought_leadership_section1:
            data['thought_leadership'].append(article.get_text().strip())

        thought_leadership_section1 = soup1.find_all('h2', class_='leadership-team')
        for article in thought_leadership_section1:
            data['thought_leadership'].append(article.get_text().strip())

        market_insights_section1 = soup1.find_all('h2', class_='market-insight-title')
        for insight in market_insights_section1:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section1 = soup1.find_all('h2', class_='market-insight')
        for insight in market_insights_section1:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section1 = soup1.find_all('h2', class_='markets')
        for insight in market_insights_section1:
            data['market_insights'].append(insight.get_text().strip())


        market_insights_section1 = soup1.find_all('h2', class_='industries')
        for insight in market_insights_section1:
            data['market_insights'].append(insight.get_text().strip())

    except requests.RequestException as err:
        print(f"Error fetching AmexGBT: {err}")

#CWT

url2 = COMPETITORS.get("mycwt")
if url2:
    processed.append("mycwt")
    print(f"Fetching mycwt at {url2}")
    try:
        response2 = requests.get(url2)
        soup2 = BeautifulSoup(response2.text, 'html.parser')

        services_section2 = soup2.find_all('h2', class_='service-title')
        for service in services_section2:
            data['service_offerings'].append(service.get_text().strip())

        services_section2 = soup2.find_all('h2', class_='our-services')
        for service in services_section2:
            data['service_offerings'].append(service.get_text().strip())

        services_section2 = soup2.find_all('h2', class_='solutions')
        for service in services_section2:
            data['service_offerings'].append(service.get_text().strip())

        services_section2 = soup2.find_all('h2', class_='what-We-offer')
        for service in services_section2:
            data['service_offerings'].append(service.get_text().strip())

        case_studies_section2 = soup2.find_all('h2', class_='case-study-title')
        for case in case_studies_section2:
            data['case_studies'].append(case.get_text().strip())

        testimonials_section2 = soup2.find_all('blockquote')
        for testimonial in testimonials_section2:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section2 = soup2.find_all('Clients')
        for testimonial in testimonials_section2:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section2 = soup2.find_all('our-work')
        for testimonial in testimonials_section2:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section2 = soup2.find_all('success-stories')
        for testimonial in testimonials_section2:
            data['client_testimonials'].append(testimonial.get_text().strip())

        thought_leadership_section2 = soup2.find_all('h2', class_='thought-leadership-title')
        for article in thought_leadership_section2:
            data['thought_leadership'].append(article.get_text().strip())

        market_insights_section2 = soup2.find_all('h2', class_='market-insight-title')
        for insight in market_insights_section2:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section2 = soup2.find_all('h2', class_='market-insight')
        for insight in market_insights_section2:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section2 = soup2.find_all('h2', class_='markets')
        for insight in market_insights_section2:
            data['market_insights'].append(insight.get_text().strip())


        market_insights_section2 = soup2.find_all('h2', class_='industries')
        for insight in market_insights_section2:
            data['market_insights'].append(insight.get_text().strip())

    except requests.RequestException as err:
        print(f"Error fetching AmexGBT: {err}")

#BCD Travel

url3 = COMPETITORS.get("bcdtravel")
if url3:
    processed.append("bcdtravel")
    print(f"Fetching bcdtravel at {url3}")
    try:
        response3 = requests.get(url3)
        soup3 = BeautifulSoup(response3.text, 'html.parser')

        services_section3 = soup3.find_all('h2', class_='service-title')
        for service in services_section3:
            data['service_offerings'].append(service.get_text().strip())

        services_section3 = soup3.find_all('h2', class_='our-services')
        for service in services_section3:
            data['service_offerings'].append(service.get_text().strip())

        services_section3 = soup3.find_all('h2', class_='solutions')
        for service in services_section3:
            data['service_offerings'].append(service.get_text().strip())

        services_section3 = soup3.find_all('h2', class_='what-We-offer')
        for service in services_section3:
            data['service_offerings'].append(service.get_text().strip())

        case_studies_section3 = soup3.find_all('h2', class_='case-study-title')
        for case in case_studies_section3:
            data['case_studies'].append(case.get_text().strip())

        testimonials_section3 = soup3.find_all('blockquote')
        for testimonial in testimonials_section3:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section3 = soup3.find_all('Clients')
        for testimonial in testimonials_section3:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section3 = soup3.find_all('our-work')
        for testimonial in testimonials_section3:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section3 = soup3.find_all('success-stories')
        for testimonial in testimonials_section3:
            data['client_testimonials'].append(testimonial.get_text().strip())

        thought_leadership_section3 = soup3.find_all('h2', class_='thought-leadership-title')
        for article in thought_leadership_section3:
            data['thought_leadership'].append(article.get_text().strip())

        market_insights_section3 = soup3.find_all('h2', class_='market-insight-title')
        for insight in market_insights_section3:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section3 = soup3.find_all('h2', class_='market-insight')
        for insight in market_insights_section3:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section3 = soup3.find_all('h2', class_='markets')
        for insight in market_insights_section3:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section3 = soup3.find_all('h2', class_='industries')
        for insight in market_insights_section3:
            data['market_insights'].append(insight.get_text().strip())

    except requests.RequestException as err:
        print(f"Error fetching AmexGBT: {err}")

#Tzell Travel

url4 = COMPETITORS.get("tzell")
if url4:
    processed.append("tzell")
    print(f"Fetching tzell at {url4}")
    try:
        response4 = requests.get(url4)
        soup4 = BeautifulSoup(response4.text, 'html.parser')

        services_section4 = soup4.find_all('h2', class_='service-title')
        for service in services_section4:
            data['service_offerings'].append(service.get_text().strip())

        services_section4 = soup4.find_all('h2', class_='our-services')
        for service in services_section4:
            data['service_offerings'].append(service.get_text().strip())

        services_section4 = soup4.find_all('h2', class_='solutions')
        for service in services_section4:
            data['service_offerings'].append(service.get_text().strip())

        services_section4 = soup4.find_all('h2', class_='what-We-offer')
        for service in services_section4:
            data['service_offerings'].append(service.get_text().strip())

        case_studies_section4 = soup4.find_all('h2', class_='case-study-title')
        for case in case_studies_section4:
            data['case_studies'].append(case.get_text().strip())

        testimonials_section4 = soup4.find_all('blockquote')
        for testimonial in testimonials_section4:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section4 = soup4.find_all('Clients')
        for testimonial in testimonials_section4:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section4 = soup4.find_all('our-work')
        for testimonial in testimonials_section4:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section4 = soup4.find_all('success-stories')
        for testimonial in testimonials_section4:
            data['client_testimonials'].append(testimonial.get_text().strip())

        thought_leadership_section4 = soup4.find_all('h2', class_='thought-leadership-title')
        for article in thought_leadership_section4:
            data['thought_leadership'].append(article.get_text().strip())

        market_insights_section4 = soup4.find_all('h2', class_='market-insight-title')
        for insight in market_insights_section4:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section4 = soup4.find_all('h2', class_='market-insight')
        for insight in market_insights_section4:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section4 = soup4.find_all('h2', class_='markets')
        for insight in market_insights_section4:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section4 = soup4.find_all('h2', class_='industries')
        for insight in market_insights_section4:
            data['market_insights'].append(insight.get_text().strip())

    except requests.RequestException as err:
        print(f"Error fetching AmexGBT: {err}")

#Egencia (part of Amex GBT)

url5 = COMPETITORS.get("egencia")
if url5:
    processed.append("egencia")
    print(f"Fetching egencia at {url5}")
    try:
        response5 = requests.get(url5)
        soup5 = BeautifulSoup(response5.text, 'html.parser')

        services_section5 = soup5.find_all('h2', class_='service-title')
        for service in services_section5:
            data['service_offerings'].append(service.get_text().strip())

        services_section5 = soup5.find_all('h2', class_='our-services')
        for service in services_section5:
            data['service_offerings'].append(service.get_text().strip())

        services_section5 = soup5.find_all('h2', class_='solutions')
        for service in services_section5:
            data['service_offerings'].append(service.get_text().strip())

        services_section5 = soup5.find_all('h2', class_='what-We-offer')
        for service in services_section5:
            data['service_offerings'].append(service.get_text().strip())

        case_studies_section5 = soup5.find_all('h2', class_='case-study-title')
        for case in case_studies_section5:
            data['case_studies'].append(case.get_text().strip())

        case_studies_section5 = soup5.find_all('h2', class_='case-studies')
        for case in case_studies_section5:
            data['case_studies'].append(case.get_text().strip())

        case_studies_section5 = soup5.find_all('h2', class_='blog')
        for case in case_studies_section5:
            data['case_studies'].append(case.get_text().strip())

        testimonials_section5 = soup5.find_all('blockquote')
        for testimonial in testimonials_section5:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section5 = soup5.find_all('Clients')
        for testimonial in testimonials_section5:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section5 = soup5.find_all('our-work')
        for testimonial in testimonials_section5:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section5 = soup5.find_all('success-stories')
        for testimonial in testimonials_section5:
            data['client_testimonials'].append(testimonial.get_text().strip())

        thought_leadership_section5 = soup5.find_all('h2', class_='thought-leadership-title')
        for article in thought_leadership_section5:
            data['thought_leadership'].append(article.get_text().strip())

        market_insights_section5 = soup5.find_all('h2', class_='market-insight-title')
        for insight in market_insights_section5:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section5 = soup5.find_all('h2', class_='market-insight')
        for insight in market_insights_section5:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section5 = soup5.find_all('h2', class_='markets')
        for insight in market_insights_section5:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section5 = soup5.find_all('h2', class_='industries')
        for insight in market_insights_section5:
            data['market_insights'].append(insight.get_text().strip())

    except requests.RequestException as err:
        print(f"Error fetching AmexGBT: {err}")

#TravelPerk

url6 = COMPETITORS.get("travelperk")
if url6:
    processed.append("travelperk")
    print(f"Fetching travelperk at {url6}")
    try:
        response6 = requests.get(url6)
        soup6 = BeautifulSoup(response6.text, 'html.parser')

        services_section6 = soup6.find_all('h2', class_='service-title')
        for service in services_section6:
            data['service_offerings'].append(service.get_text().strip())

        services_section6 = soup6.find_all('h2', class_='our-services')
        for service in services_section6:
            data['service_offerings'].append(service.get_text().strip())

        services_section6 = soup6.find_all('h2', class_='solutions')
        for service in services_section6:
            data['service_offerings'].append(service.get_text().strip())

        services_section6 = soup6.find_all('h2', class_='discover-our-solutions')
        for service in services_section6:
            data['service_offerings'].append(service.get_text().strip())

        services_section6 = soup6.find_all('h2', class_='what-We-offer')
        for service in services_section6:
            data['service_offerings'].append(service.get_text().strip())

        case_studies_section6 = soup6.find_all('h2', class_='case-study-title')
        for case in case_studies_section6:
            data['case_studies'].append(case.get_text().strip())

        testimonials_section6 = soup6.find_all('blockquote')
        for testimonial in testimonials_section6:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section6 = soup6.find_all('Clients')
        for testimonial in testimonials_section6:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section6 = soup6.find_all('our-work')
        for testimonial in testimonials_section6:
            data['client_testimonials'].append(testimonial.get_text().strip())

        testimonials_section6 = soup6.find_all('success-stories')
        for testimonial in testimonials_section6:
            data['client_testimonials'].append(testimonial.get_text().strip())

        thought_leadership_section6 = soup6.find_all('h2', class_='thought-leadership-title')
        for article in thought_leadership_section6:
            data['thought_leadership'].append(article.get_text().strip())

        market_insights_section6 = soup6.find_all('h2', class_='market-insight-title')
        for insight in market_insights_section6:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section6 = soup6.find_all('h2', class_='market-insight')
        for insight in market_insights_section6:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section6 = soup6.find_all('h2', class_='markets')
        for insight in market_insights_section6:
            data['market_insights'].append(insight.get_text().strip())

        market_insights_section6 = soup6.find_all('h2', class_='industries')
        for insight in market_insights_section6:
            data['market_insights'].append(insight.get_text().strip())

    except requests.RequestException as err:
        print(f"Error fetching AmexGBT: {err}")

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

print(data)