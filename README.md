# Amazon Review Analyzer

An intelligent Python application that scrapes Amazon product reviews, analyzes sentiment using AI, and generates comprehensive insights. This tool combines web scraping, natural language processing, and modern LLM APIs to provide actionable review analysis in CSV format.

## Features

- **Automated Web Scraping**: Extracts customer reviews, ratings, dates, and metadata from Amazon product pages
- **AI-Powered Analysis**: Uses Groq's Llama 3.3 model for sentiment analysis and review summarization  
- **Robust Error Handling**: Continues processing even if individual reviews fail to analyze
- **Structured Output**: Saves results in clean CSV format with organized columns
- **Progress Tracking**: Real-time feedback during scraping and analysis phases
- **Rate Limiting**: Built-in delays to avoid anti-bot detection
- **Environment Configuration**: Secure API key management using .env files

## Installation

### Prerequisites

- Python 3.8 or higher
- Groq API account (free tier available)
- Virtual environment (recommended)

### Setup Steps

1. **Clone or download the project**:
   ```bash
   cd review_analyzer
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (see Configuration section below)

## Configuration

Create a `.env` file in the project root with your API credentials:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Getting Your Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account (no credit card required)
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key to your `.env` file

## Usage

### Basic Usage

Run the application and enter an Amazon product URL when prompted:

```bash
python main.py
```

### Example Amazon URL Format

Use any Amazon product page URL that has customer reviews:
```
https://www.amazon.in/product-name/dp/PRODUCT_ID/
```

### Sample Output

The application will:
1. Scrape reviews from the provided URL
2. Analyze each review using AI
3. Save results to `results/analyzed_reviews_TIMESTAMP.csv`

**Console Output:**
```
Starting analysis for : https://amazon.in/example-product/...
processing upto 10 reviews
Scraping reviews...
Found 8 reviews. Starting analysis...
 Analyzing review 1/8...
   ✅ Review 1 analyzed successfully

 Analyzing review 2/8...
   ✅ Review 2 analyzed successfully
...
Analysis complete. Results saved to results/analyzed_reviews_20241203_203045.csv
```

## CSV Output Structure

| Column | Description |
|--------|-------------|
| original_text | Full customer review text |
| rating | Star rating (1-5) |
| date | Review publication date |
| sentiment | AI-analyzed sentiment (Positive/Negative/Neutral) |
| summary | AI-generated 1-2 sentence summary |

## Example Product URL Used

For development and testing, I used:
```
https://www.amazon.in/TechPride-Curtain-Hanging-Bedroom-Decorations/dp/B0DFQL9FZL/
```

This LED curtain light product page provided diverse reviews with varying sentiments, making it ideal for testing the analysis capabilities.

## Design Choices

### Web Scraping Approach
- **BeautifulSoup over Selenium**: Chosen for faster execution and lower resource usage
- **Custom selectors**: Discovered actual Amazon CSS classes through manual inspection
- **User-Agent spoofing**: Prevents bot detection with realistic browser headers

### LLM Integration  
- **Groq over OpenAI**: Selected for faster response times and generous free tier
- **Llama 3.3-70B model**: Balances quality and speed for review analysis
- **Structured prompts**: Uses clear format instructions for consistent AI responses

### Error Handling Strategy
- **Graceful degradation**: Failed review analyses don't stop the entire process  
- **Comprehensive try-catch**: Separate error handling for scraping and AI analysis
- **User feedback**: Clear progress indicators and error messages

### Data Storage
- **CSV format**: Universal compatibility and easy data analysis
- **Timestamped files**: Prevents overwriting previous analyses
- **Organized structure**: Results folder keeps outputs clean

## Limitations

### Technical Limitations
- **Amazon's anti-bot measures**: May require occasional selector updates
- **Rate limiting**: Processing large numbers of reviews takes time
- **API dependencies**: Requires internet connection and Groq API availability

### Scope Limitations  
- **Amazon-specific**: Currently only supports Amazon product pages
- **English reviews**: AI analysis optimized for English text
- **Review pagination**: Processes reviews from first page only

### Data Quality
- **Truncated reviews**: Some reviews may be shortened by Amazon's "Read more" feature
- **AI consistency**: Sentiment analysis may vary slightly between runs
- **Network reliability**: Dependent on stable internet connection

## Future Improvements

### Enhanced Features
- **Multi-site support**: Extend to other e-commerce platforms (eBay, Walmart)
- **Review pagination**: Scrape multiple pages of reviews automatically  
- **Advanced analytics**: Add keyword extraction, theme analysis, pros/cons identification
- **Export formats**: Support JSON, Excel, and database storage options

### Performance Optimizations
- **Async processing**: Parallel review analysis for faster execution
- **Caching system**: Store processed reviews to avoid re-analysis
- **Batch processing**: Handle multiple product URLs in single execution

### User Experience
- **GUI interface**: Web-based dashboard for non-technical users
- **Configuration UI**: Easy setup without manual .env file editing
- **Real-time visualization**: Charts and graphs of sentiment trends

## Dependencies

- **requests**: HTTP requests for web scraping
- **beautifulsoup4**: HTML parsing and data extraction  
- **groq**: Groq LLM API client
- **pandas**: Data manipulation and CSV export
- **python-dotenv**: Environment variable management

## License

This project is created for educational and portfolio purposes.

