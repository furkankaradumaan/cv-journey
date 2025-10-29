#!/bin/bash

python3 test_scrape_pages.py # Test the scrape_pages method
python3 test_scrape_page.py
pytest test_quotes_class.py
pytest test_page_url_creator.py
pytest test_extract_data.py
pytest test_analyzer.py