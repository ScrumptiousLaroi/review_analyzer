import requests
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
import re

def scrape_reviews(url, max_reviews = 50):
    """Scrape reviews from amazon product url,
    url : amazon product url,
    max_reviews : maximum number of reviews to scrape,
    Returns a list of review dictionaries
    """
     # Set up headers to look like a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    # Check robots.txt
    rp = RobotFileParser()
    rp.set_url("https://www.amazon.in/robots.txt")
    rp.read()
    allowed = rp.can_fetch(headers['User-Agent'], url)
    #  Make the request if allowed
    if allowed:
        try: 
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            return []
    else:
        print("Scraping not allowed by robots.txt")
        return []
    
    #  Parse with BeautifulSoup  
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all reviews using your selectors
    reviews = []
    review_containers = soup.find_all('div', class_='a-section celwidget')

    # Filter to only actual reviews (they have customer_review in ID)
    review_containers = [div for div in review_containers if div.get('id', '').startswith('customer_review')]

    print(f"Found {len(review_containers)} reviews")

    # Step 5: Extract data from each review
    for container in review_containers[:max_reviews]:
        review_data = {}

        text_element = container.find('div', class_='a-expander-content reviewText review-text-content a-expander-partial-collapse-content')
        review_data['text'] = text_element.get_text().strip() if text_element else "No text"

        rating_element = container.find(class_='review-rating')
        if rating_element:
            rating_text = rating_element.get_text()
            review_data['rating'] = rating_text.split()[0]
        else:
            review_data['rating'] = "No rating"

        date_element = container.find(class_='review-date')
        review_data['date'] = date_element.get_text().strip() if date_element else "No date"

        reviews.append(review_data)


    #  Return list of review dictionaries
    return reviews