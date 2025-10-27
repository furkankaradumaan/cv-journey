"""
Web Scraper Project - Week 1
A simple web scraping tool with error handling and data export.

Scrapes book data from http://quotes.toscrape.comand performs analysis
on this data using Pandas.
"""

from abc import ABC, abstractmethod # For creating abstract classes.
from bs4 import BeautifulSoup, Tag # For parsing HTML data.
import csv # For saving book data in CSV files.
from dataclasses import dataclass, field
import json # For loading book data in JSON files.
import pandas as pd # For converting book data into DataFrames and make analysis.
from typing import Dict, List, Optional # For type hints.

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
        pass

class BasePageScraper(ABC):
    """
    This is an abstract base class for Scraper classes
    """
    @abstractmethod
    def extractData(element: Tag):
        """
        Extracts the desired data from given element.
        """
        pass

    @abstractmethod
    def scrapePage(url: str):
        pass

class QuoteScraper(BasePageScraper):
    """
    This class will scrape the quotes in given URL.
    """
    def extractData(element: Tag) -> Optional[Quote]:
        """
        Extracts the book data from given Tag.
        """
        pass

    def scrapePage(url: str) -> List[Quote]:
        """
        Scrapes all the quotes in the given page.
        """
        pass

class QuoteAnalyzer:
    """
    Analysis the given 
    """
    def __init__(self, quotes: List[Quote]):
        self.__quotes = quotes
        self.__filtered = quotes[:] # Initially, holds the copy of quotes.
    
    def minimumLength(self, minLength: int) -> "QuoteAnalyzer":
        """
        Filters the quotes whose length is greater than or equal to the minLength.
        The filter operations are performed on __filtered list.
        Returns the object itself.
        """
        pass
    
    def maximumLength(self, maxLength) -> "QuoteAnalyzer":
        """
        Filters the quotes whose length is smaller than or equal to the maxLength.
        The filter operations are performed on __filtered list.
        Returns the object itself.
        """
        pass

    def byAuthor(self, author: str) -> "QuoteAnalyzer":
        """
        Filters the quotes whose author name is same as the given author.
        The filter operations are performed on __filtered list.
        Returns the object itself.
        """
        pass

    def byTag(self, tag: str) -> "QuoteAnalyzer":
        """
        Filters the quotes whose contains the specified tag.
        The filter operations are performed on __filtered list.
        Returns the object itself.
        """
        pass

    def clearFilters(self) -> "QuotesAnalyzer":
        """
        This function clears all the filters made on __filtered.
        Returns the object itself.
        """
        pass

    def get(self) -> List[Quote]:
        """
        Returns filtered list.
        """
        pass

    def count(self) -> int:
        """
        Returns the number of elements in filtered list.
        """
        pass

class QuoteWriter:
    """
    This class is responsible for writing quotes data into
    vairous formats (CSV, JSON).
    """
    @staticmethod
    def toJSON(quotes: List[Quote], jsonName: str):
        """
        Writes the quote data into a JSON file with given name.
        """
        pass

    @staticmethod
    def toCSV(quotes: List[Quote], csvName: str):
        """
        Writes the quote data into a CSV file with given name.
        """
        pass

def main():
    """
    Calls scrape method of Scraper class to scrape book data from
    the page. Calls toJSON and toCSV functions to save the book data
    both in CSV and JSON format. Then creates an analyzer and analysis the
    data.
    """
    pass

if __name__ == "__main__":
    main()
