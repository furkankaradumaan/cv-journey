"""
Web Scraper Project - Week 1
A simple web scraping tool with error handling and data export.

Scrapes book data from http://quotes.toscrape.comand performs analysis
on this data using Pandas.
"""

from abc import ABC, abstractmethod # For creating abstract classes.
from typing import Any, List, Optional # For type hints.
import logging
import csv # For saving book data in CSV files.
from dataclasses import dataclass, field
from urllib.parse import urljoin
import json # For loading book data in JSON files.
from bs4 import BeautifulSoup, Tag # For parsing HTML data.
import pandas as pd # For converting book data into DataFrames and make analysis.
import requests # To make GET requests to web pages.
import sys

# Dosyanın en üstünde
logging.basicConfig(
    format="%(levelname)s:%(name)s:%(message)s", # Düzeltildi: mesaj bitimine %s eklendi
    filename="logs.log", 
    filemode="a",
    level=logging.INFO # Düzeltildi: INFO seviyesindeki mesajları aktif eder
)
logger = logging.getLogger(__name__)

class QuoteValueInvalidException(ValueError):
    """
    Raised when quote text or author is None or have length of 0.
    """

## TESTED and SUCCESSFULL
@dataclass
class Quote:
    """
    This class represents a Quote.
    Contains fields:
       * author: Person who has the quote.
       * text  : The quote text.
       * tags  : A list of all tags related to the quote.
    """
    text: str = field(default=None)
    author: str = field(default=None)
    tags: List[str] = field(default_factory=lambda: [])
   
    def __post_init__(self):
        """
        This function used for validating quote data.
        If any of the values are not valid, a QuoteValueInvalidException is raised.
        """
        if self.text is None:
            raise QuoteValueInvalidException("Text attribute is None")
        elif self.author is None:
            raise QuoteValueInvalidException("Author attribute is None")
        elif self.tags is None:
            raise QuoteValueInvalidException("Tags attribute is None")

        self.text = self.text.strip()
        self.author = self.author.strip()
        if len(self.text) == 0 or len(self.author) == 0:
            raise QuoteValueInvalidException("Text or author has a length of zero.")

## TESTED and SUCCESSFULL
class PageURLCreator:
    """
    This class is responsible for creating different
    URL's for differrent pages, according to given URL.
    """
    def __init__(self, baseurl: str):
        self.__baseurl = baseurl

    def create_url_of_page_number(self, page: int) -> str:
        """
        Creates a page URL in the form of "<baseurl>/page/<page_number>"
        """
        return urljoin(self.__baseurl, f"page/{page}")

    @property
    def baseurl(self):
        """Get baseurl"""
        return self.__baseurl

    @baseurl.setter
    def baseurl(self, url: str):
        self.url = url

## TESTED and SUCCESSFULL

class BaseMultiPageScraper(ABC):
    """
    This is an abstract base class for a Scraper class which can scrape multiple pages
    """
    def __init__(self, url_creator: PageURLCreator):
        self.url_creator = url_creator

    @abstractmethod
    def extract_data(self, element: Tag) -> Optional[Any]:
        """
        Extracts the desired data from given element.
        """

    @abstractmethod
    def scrape_page(self, soup: BeautifulSoup) -> List[Any]:
        """
        Scrapes all the data in the given soup object.
        """

    ## TESTED and SUCCESSFULL
    def scrape_pages(self, start_page: int, end_page:  int) -> List[Any]:
        """
        Scrapes data from all the pages starting from page startPage to endPage.
        """
        logger.info("Started scraping pages")
        obj_list = [] # Empty list initially

        for page in range(start_page, end_page+1):
            # Create the URL for current page
            logger.info("Fetching page")
            page_url = self.url_creator.create_url_of_page_number(page)
            response = requests.get(page_url, timeout=10)
            if response.status_code != 200:
                logger.info(f"Page data could not fetched: {page_url}")
                continue
            soup = BeautifulSoup(response.content, "html.parser")
            logger.info(f"Scraping page: {page_url}")
            obj_list.extend(self.scrape_page(soup))

        return obj_list

## TESTED and SUCCESSFULL
class QuoteScraper(BaseMultiPageScraper):
    """
    This class will scrape the quotes in given URL.
    """

    # TESTED and SUCCESSFULL
    def extract_data(self, element: Tag) -> Optional[Quote]:
        """
        Extracts the book data from given Tag.
        """
        # span tag with class "text" contains the text of the quote
        span_tag = element.find("span", class_="text")
        if span_tag is None:
            return None
        text = span_tag.get_text()

        # The author name is written in a small tag with class "author"
        small_tag = element.find("small", class_="author")
        if small_tag is None:
            return None
        author = small_tag.get_text()
        
        # Tags are put in a div tag contains all the tags.
        # Each tag written in a "a" tag with class tag.
        tags = []
        a_tags = element.find_all("a", class_="tag")
        for a_tag in a_tags:
            tags.append(a_tag.get_text())
        
        return Quote(text=text, author=author, tags=tags) # Create and return the quote object.
    
    # TESTED and SUCCESSFULL
    def scrape_page(self, soup: BeautifulSoup) -> List[Quote]:
        """
        Scrapes all the quotes in the given page.
        """
        # All quotes are packaged in div tags with class "quote"
        quotes_in_page = []
        quote_divs = soup.find_all("div", class_="quote")
        logger.info(f"Found {len(quote_divs)} quotes")
        for count, quote_div in enumerate(quote_divs):
            logger.info("Found a new quote div. Extracting data inside")
            quote = self.extract_data(quote_div)
            if quote is not None:
                logger.info("Successfully extracted, adding into list")
                quotes_in_page.append(quote)
            else:
                print(f"Quote {count+1} is None")
        return quotes_in_page

class QuoteAnalyzer:
    """
    Analysis the given 
    """
    def __init__(self, quotes: List[Quote]):
        self.__quotes_df = pd.DataFrame(
            {
                "text": [quote.text for quote in quotes],
                "author": [quote.author for quote in quotes],
                "tags": [quote.tags for quote in quotes]
            }
        )
        self.__filtered = self.__quotes_df.copy()
    
    def minimum_length(self, min_length: int, negate=False) -> "QuoteAnalyzer":
        """
        Filters the quotes whose length is greater than or equal to the minLength.
        The filter operations are performed on __filtered list.
        if negate choice is active, converts the condition to its negation.
        Returns the object itself.
        """
        lengths = self.__filtered["text"].str.len()
        condition = lengths >= min_length
        
        if negate:
            condition = ~condition
        
        self.__filtered = self.__filtered[condition]
        return self        
    
    def maximum_length(self, max_length, negate=False) -> "QuoteAnalyzer":
        """
        Filters the quotes whose length is smaller than or equal to the maxLength.
        The filter operations are performed on __filtered list.
        if negate choice is active, converts the condition to its negation.
        Returns the object itself.
        """
        lengths = self.__filtered["text"].str.len()

        condition = lengths <= max_length
        if negate:
            condition = ~condition
        
        self.__filtered = self.__filtered[condition]
        return self

    def by_author(self, author: str, negate=False) -> "QuoteAnalyzer":
        """
        Filters the quotes whose author name is same as the given author.
        The filter operations are performed on __filtered list.
        if negate choice is active, converts the condition to its negation.
        Returns the object itself.
        """
        condition = self.__filtered["author"] == author
        if negate:
            condition = ~condition
        self.__filtered = self.__filtered[condition]
        return self

    def by_tag(self, tag: str, negate=False) -> "QuoteAnalyzer":
        """
        Filters the quotes whose contains the specified tag.
        The filter operations are performed on __filtered list.
        if negate choice is active, converts the condition to its negation.
        Returns the object itself.
        """
        condition = self.__filtered["tags"].apply(lambda tags: tag in tags)
        if negate:
            condition = ~condition
        self.__filtered = self.__filtered[condition]
        return self

    def clear_filters(self) -> "QuotesAnalyzer":
        """
        This function clears all the filters made on __filtered.
        Returns the object itself.
        """
        self.__filtered = self.__quotes_df.copy() # Assign a copy of actual quotes list
        return self

    def get(self) -> pd.DataFrame:
        """
        Returns filtered list.
        """
        return self.__filtered.copy() # Return a copy of filtered quotes

    def get_column(self, column) -> pd.Series:
        """
        Returns desired column in __filtered data
        """
        return self.__filtered[column]
    
    def count(self) -> int:
        """
        Returns the number of elements in filtered list.
        """
        return len(self.__filtered.index)

class QuoteWriter:
    """
    This class is responsible for writing quotes data into
    vairous formats (CSV, JSON).
    """
    @staticmethod
    def to_json(quotes: List[Quote], json_name: str):
        """
        Writes the quote data into a JSON file with given name.
        """
        with open(json_name, "w", encoding="utf-8") as jsonfile:
            json.dump([
                {"text": quote.text, "author": quote.author, "tags": quote.tags} for quote in quotes
            ], jsonfile, indent=4)

    @staticmethod
    def to_csv(quotes: List[Quote], csv_name: str):
        """
        Writes the quote data into a CSV file with given name.
        """
        with open(csv_name, "w", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile,
                fieldnames=["text", "author", "tags"]
            )
            writer.writeheader()
            writer.writerows(
                [{"text": quote.text, "author": quote.author, "tags": quote.tags} for quote in quotes]
                )

def main():
    """
    Calls scrape method of Scraper class to scrape book data from
    the page. Calls toJSON and toCSV functions to save the book data
    both in CSV and JSON format. Then creates an analyzer and analysis the
    data.
    """
    baseurl = "http://quotes.toscrape.com"
    csv_name = "quotes.csv"
    json_name = "quotes.json"
    start_page = 1
    end_page = 5

    url_creator = PageURLCreator(baseurl=baseurl)
    scraper = QuoteScraper(url_creator=url_creator)
    quotes = scraper.scrape_pages(start_page, end_page)

    QuoteWriter.to_csv(quotes, csv_name)
    print(f"\u2713 Saved {len(quotes)} quotes in {csv_name}")
    QuoteWriter.to_json(quotes, json_name)
    print(f"\u2713 Saved {len(quotes)} quotes in {json_name}")

    if len(quotes) == 0:
        print("No quotes to analyze")
        return
    analyzer = QuoteAnalyzer(quotes)

    print("="*70)
    print("QUOTE ANALYZER".center(70))
    print("="*70)

    # < --- Some Analysis on Data --- >
    print(f"Number of quotes: {len(analyzer.get().index)}")
    # Get the text column, take the lengths of all column, calculate the average.
    print(f"Average quote length: {analyzer.get_column("text").apply(len).mean()}")


if __name__ == "__main__":
    main()
