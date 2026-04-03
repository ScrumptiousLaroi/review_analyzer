import os
from groq import Groq
from dotenv import load_dotenv

def analyze_review(review_text):
    """ Analyze review text using Groq and return sentiment and summary. 
    Args:
        review_text (str): The text of the review to analyze.
    Returns:
        dict: A dictionary containing the sentiment and summary of the review.
    """
    load_dotenv() 
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in your .env file.")
    # Step 2: Create analysis prompt  
    prompt = f"""Analyze this product review. Provide:
        1. Sentiment: positive/negative/neutral
        2. Summary: 1-2 sentences highlighting key points

        Review: {review_text}
        """
    # Step 3: Send to Groq API
    try:
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=200
        )
        ai_response = response.choices[0].message.content
    except Exception as e:
        return {"sentiment": "Error", "summary": f"API call failed: {str(e)}"}
    # Step 4: Parse response
    try:
        lines = ai_response.splitlines()
        sentiment = "neutral" #default
        summary = "No summary"
        for line in lines:
            if "sentiment:" in line.lower():
                sentiment_part = line.lower().split("sentiment:")[-1].strip()
                if "positive" in sentiment_part:
                    sentiment = "Positive"
                elif "negative" in sentiment_part:
                    sentiment = "Negative"
                elif "neutral" in sentiment_part:
                    sentiment = "Neutral"
            elif "summary:" in line.lower():
                summary = line.split("summary:")[-1].strip()
        
        return {"sentiment": sentiment, "summary": summary}
    except Exception as e:
        return {"sentiment": "Error", "summary": f"parsing error: {str(e)}"}
   