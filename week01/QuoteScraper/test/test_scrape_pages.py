"""
This program will test the scrape_pages method
of BaseMultiPageScraper class.
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import scraper
from scraper import QuoteScraper

class Test(unittest.TestCase):
    """Test Cases"""
    def test_scrape_pages_success(self):
        """
        This function tests scraper pages function.
        """
        with (patch("scraper.requests.get") as get_mock,
              patch("scraper.QuoteScraper.scrape_page") as scrmock
            ):
            
            start_page = 1
            end_page = 3
            total_pages = end_page - start_page + 1

            # 1. urlmock: Sıralı URL'ler döndür
            urlmock = Mock()
            urlmock.create_url_of_page_number.side_effect = [
                f"https://page.com/{p}" for p in range(start_page, end_page + 1)
            ]
            
            mock_responses = []
            for _ in range(total_pages):
                response_mock = MagicMock()
                response_mock.status_code = 200
                response_mock.content = b"<p> Hello, world! </p>"
                mock_responses.append(response_mock)
            get_mock.side_effect = mock_responses

            # 3. scrmock: Her çağrıda farklı (veya aynı) Quote listesi döndür
            quotes_page_1 = [scraper.Quote("T1", "A1", ["tag1"])]
            quotes_page_2 = [scraper.Quote("T2", "A2", ["tag2", "tag3"])]
            quotes_page_3 = [scraper.Quote("T3", "A3", ["tag4"])]

            scrmock.side_effect = [quotes_page_1, quotes_page_2, quotes_page_3]

            expected_data = quotes_page_1 + quotes_page_2 + quotes_page_3

            obj = scraper.QuoteScraper(urlmock)
            data = obj.scrape_pages(start_page, end_page)

            # < --- Assertions --- >
            self.assertEqual(data, expected_data, "The data is wrong.")

            # < --- Check the call counts for the dependencies --- >
            # They should have called total_pages times
            self.assertEqual(urlmock.create_url_of_page_number.call_count, total_pages, "Function call count should be same as total pages")
            self.assertEqual(get_mock.call_count, total_pages, "GET function should be called as total pages")
            self.assertEqual(scrmock.call_count, total_pages, "scrape_page function shoul be called as total pages")

    def test_scrape_pages_failed_request(self):
        """Tests the scrape_pages function with failed requests"""
        with (patch("scraper.requests.get") as get_mock,
              patch("scraper.QuoteScraper.scrape_page") as scr_mock):
            
            start_page = 1
            end_page = 3
            total_pages = end_page - start_page + 1
            
            # < --- Set urlmock -->
            url_mock = Mock()
            url_mock.create_url_of_page.side_effect = [
                f"https://page{p}" for p in range(start_page, end_page+1)
            ]
            
            # < --- Mock the GET requests --->
            mock_responses = []
            for _ in range(start_page, end_page+1):
                response_mock = MagicMock()
                response_mock.status_code = 404 # Request not successfull
                response_mock.content = b"<p> Hello </p>"
                mock_responses.append(response_mock)
            get_mock.side_effect = mock_responses
            
            # < --- Mock the responses of scrape_page function --- >
            quotes_page_1 = [scraper.Quote("T1", "A1", ["tag1"])]
            quotes_page_2 = [scraper.Quote("T2", "A2", ["tag2", "tag3"])]
            quotes_page_3 = [scraper.Quote("T3", "A3", ["tag4"])]

            scr_mock.side_effect = [quotes_page_1, quotes_page_2, quotes_page_3]

            expected_data = [] # Since we expect all the pages will be skipped (because GET request failed)

            obj = QuoteScraper(url_mock)
            data = obj.scrape_pages(start_page, end_page)

            # < --- Assert the equality of data and expected data --- >
            self.assertEqual(data, expected_data, "Data and expected data should be equal")

            # < --- Now we will check the call counts of the mock objects --- >
            # Since our status code is always invalid, we will skip the every loop
            # after checking the status code of the GET request.
            # So the create_url_of_page function will be called total_pages times,
            # the get method of requests will be called total_pages times, but
            # the scrape_page method will never be called.
            self.assertEqual(url_mock.create_url_of_page_number.call_count, total_pages)
            self.assertEqual(get_mock.call_count, total_pages)
            self.assertEqual(scr_mock.call_count, 0) # This shouldn't be called

if __name__ == "__main__":
    unittest.main()