from scraper import scrape_reviews

url = "https://www.amazon.in/TechPride-Curtain-Hanging-Bedroom-Decorations/dp/B0DFQL9FZL/?_encoding=UTF8&pd_rd_w=laB3g&content-id=amzn1.sym.f0f176ce-9420-4dd6-a9d1-fed20e5ad5d8&pf_rd_p=f0f176ce-9420-4dd6-a9d1-fed20e5ad5d8&pf_rd_r=6VZCCNEHXW29HD7PMYCS&pd_rd_wg=RvfZ0&pd_rd_r=4a669f92-4a31-40bc-bbfc-b7d580983c74&ref_=pd_hp_d_atf_dealz_sv&th=1"  # You'll need a real URL
reviews = scrape_reviews(url, max_review=5)  # Just test with 5 reviews

print(f"Found {len(reviews)} reviews")
for i, review in enumerate(reviews):
    print(f"Review {i+1}:")
    print(f"  Text: {review['text']}")  
    print(f"  Rating: {review['rating']}")
    print(f"  Date: {review['date']}")
    print()