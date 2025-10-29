# Web Scraper Project - QuoteScraper

Professional multi-page web scraping tool with OOP design, type safety, and data analysis capabilities.

## 🎯 Project Overview

Scrapes quotes from http://quotes.toscrape.com with a robust, extensible architecture suitable for production use.

## ✨ Key Features

- **Object-Oriented Design**: Abstract base classes for extensibility
- **Type Safety**: Comprehensive type hints throughout
- **Error Handling**: Custom exceptions and validation
- **Logging System**: Professional debugging and monitoring
- **Data Analysis**: Pandas-based analysis with fluent API
- **Export Formats**: CSV and JSON support
- **Unit Tested**: All components thoroughly tested

## 🏗️ Architecture
QuoteScraper/
├── PageURLCreator       # URL generation
├── BaseMultiPageScraper # Abstract scraper interface
├── QuoteScraper         # Quote-specific implementation
├── QuoteAnalyzer        # Data analysis with method chaining
└── QuoteWriter          # Export functionality

## 🔧 Technologies

- Python 3.12
- BeautifulSoup4 - HTML parsing
- Requests - HTTP requests
- Pandas - Data manipulation & analysis
- Logging - Professional debugging

## 📦 Installation
```bash
pip install -r requirements.txt
```

## 🚀 Usage
```python
# Basic scraping
url_creator = PageURLCreator(baseurl="http://quotes.toscrape.com")
scraper = QuoteScraper(url_creator=url_creator)
quotes = scraper.scrape_pages(start_page=1, end_page=5)

# Save to files
QuoteWriter.to_csv(quotes, "quotes.csv")
QuoteWriter.to_json(quotes, "quotes.json")

# Analyze data
analyzer = QuoteAnalyzer(quotes)
filtered = analyzer.minimum_length(50).by_author("Einstein").get()
print(f"Found {analyzer.count()} quotes")
```

## 📊 Example Output
```
✓ Saved 100 quotes in quotes.csv
✓ Saved 100 quotes in quotes.json

======================================================================
                           QUOTE ANALYZER                            
======================================================================
Number of quotes: 100
Average quote length: 87.3
```

## 🎨 Code Highlights

### dataclasses with attribute validation
[Quote dataclass](images/carbon.png)
The Quote dataclass provides a good way to represent the Quote data:
It also validates if there is None attribute.
```python
quote = Quote(text="Python is beautiful", author="Furkan Karaduman", tags=["python", "programming"])
```

## 👤 Author

Furkan Karaduman - Week 1 Project
Computer Vision Learning Journey

---
