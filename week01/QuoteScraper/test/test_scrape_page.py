"""
This program tests the scrap_page method
of QuoteScraper class.
"""

from bs4 import BeautifulSoup
import unittest
from unittest.mock import patch, Mock
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import scraper

class TestScrapePageMethod(unittest.TestCase):
    """
    Tests the scrape_page method in QuoteScraper class.
    """

    def _create_mock_soup(self):
        """Creates an HTML content to produce a mock BeautfiulSoup object."""
        html_content = """
        <html>
            <body>
                <div class="col-md-8">
                    <div class="quote" id="q1"> </div>
                    <div class="quote" id="q2"> </div>
                    <div class="quote" id="q3"> </div>
                    <div class="quote" id="q4"> </div>
                </div>
            </body>
        </html>
        """
        return BeautifulSoup(html_content, "html.parser")
    
    def test_scrape_page_successfull(self):
        """Tests the scrape_page method for successfull cases (no quote object is None)"""

        with patch("scraper.QuoteScraper.extract_data") as extract_mock:
            # < --- Prepare quotes that will be scraped --- >
            quote1 = scraper.Quote(text="Text1", author="Author1", tags=["a", "b"])
            quote2 = scraper.Quote(text="Text2", author="Author2", tags=["a"])
            quote3 = scraper.Quote(text="Text3", author="Author3", tags=["a", "b", "c"])
            quote4 = scraper.Quote(text="Text4", author="Author4", tags=[])

            expected_quotes = [quote1, quote2, quote3, quote4]

            # extract_data function will return every item in this list in order
            # everytime it is called.
            extract_mock.side_effect = expected_quotes

            # < --- Create a mock soup object --- >
            test_soup = self._create_mock_soup()

            # < --- Create an instance of QuoteScraper --- >
            # We will simply mock the url_creator, it is not important in here.
            test_scraper = scraper.QuoteScraper(url_creator=Mock())

            # Now call the scrape_page method with giving the test_soup object.
            # This will return a list that contains all the quotes in the list.
            actual_quotes = test_scraper.scrape_page(test_soup)

            # < --- Assertions --- >
            # Now we will test the data we got.
            self.assertEqual(actual_quotes, expected_quotes, "actual_quotes is not same as expected quotes")

            # Now we will check the number of call counts
            # of our mock extract_data method. It should be called
            # as many as the quote count (valid_quotes + invalid_quotes)
            self.assertEqual(extract_mock.call_count, 4) # In this case we have total 4 quotes.

if __name__ == "__main__":
    unittest.main()