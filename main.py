import os
from scraper import scrape_reviews
from analyzer import analyze_review
import pandas as pd
from datetime import datetime

def analyze_product_reviews(url, max_reviews = 50):
    """
    scrape reviews, analyzes them with ai, and returns a csv
    Args:
        url (str): The URL of the product reviews page on Amazon.
        max_reviews (int): The maximum number of reviews to scrape and analyze. 
    Returns:
        str: The filename of the generated CSV file containing the reviews and their analysis.
    """

    print(f"Starting analysis for : {url}")
    print(f"processing upto {max_reviews} reviews")

    # Step 1: Scrape reviews
    print("Scraping reviews...")
    reviews = scrape_reviews(url, max_reviews=max_reviews)

    if not reviews:
        print("No reviews found. Please check the URL and try again.")
        return None
    
    print(f"Found {len(reviews)} reviews. Starting analysis...")
    # Step 2: Analyze each review
    analyzed_reviews = []

    for i, review in enumerate(reviews, 1):
        print(f" Analyzing review {i}/{len(reviews)}...")

        try:
            analysis = analyze_review(review['text'])

            complete_review = {
                'original_text': review['text'],
                'rating': review['rating'],
                'date': review['date'],
                'sentiment': analysis['sentiment'],
                'summary': analysis['summary']
            }
            analyzed_reviews.append(complete_review)

        except Exception as e:
            print(f"Error analyzing review {i}: {e}")
            continue
        if not analyzed_reviews:
            print("⚠️ No reviews were successfully analyzed!")
            return None
    # Step 3: Store results in csv
    if analyzed_reviews:
        df = pd.DataFrame(analyzed_reviews)

        results_dir = "results"
        os.makedirs(results_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"analyzed_reviews_{timestamp}.csv"

        filepath = os.path.join(results_dir, filename)
        df.to_csv(filepath, index=False)
        print(f"Analysis complete. Results saved to {filename}")
        return filename



if __name__ == "__main__":
    url = input("Enter the Amazon product reviews URL: ")
    results = analyze_product_reviews(url, max_reviews=10)