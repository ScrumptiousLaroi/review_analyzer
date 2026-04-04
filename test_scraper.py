from scraper import scrape_reviews

url = "https://www.amazon.in/iPhone-Pro-256-Promotion-Breakthrough/dp/B0FQG1LPVF/ref=sr_1_1_sspa?crid=CDERI31QBMK7&dib=eyJ2IjoiMSJ9.GtbzqrOW2c9P1QmN-FL-P4M9VrvPoTOnlK326bKQOxUu1UE0EJkQKTexZUcwvLYuyCqfzGVB5Zl90iDz32g_OOTy0twhweQ3VKugF_aElwdmuh9a4Z5Jnxc21D4I-XaeWq9Rb_Jlod8rHArBMg9U4uqMr5yVMlcY4wPHAwlFV4rxrBnNAssG4D8njlsPOt6ILbb9ForxrFET3YflKN3dbHPfF1VgYF-G7aE3lt_W4Bw.k-Igp3DzkDm6sT0C9bLq-GxsYO4THiPz9GHliHiv2IU&dib_tag=se&keywords=iphone%2B17%2Bpro&qid=1775309519&sprefix=%2Caps%2C382&sr=8-1-spons&aref=QtLHym9213&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
reviews = scrape_reviews(url, max_reviews=5)  # Just test with 5 reviews

print(f"Found {len(reviews)} reviews")
for i, review in enumerate(reviews):
    print(f"Review {i+1}:")
    print(f"  Text: {review['text']}")  
    print(f"  Rating: {review['rating']}")
    print(f"  Date: {review['date']}")
    print()