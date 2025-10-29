"""
This program checks the PageURLCreater class.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper import PageURLCreator


@pytest.fixture
def url_creator():
    """
    This function returns a PageURLCreator object, seperately for each test case.
    """
    return PageURLCreator(baseurl="https://quotes.toscrape.com/")

@pytest.mark.parametrize("page_number, expected",
[
    (1, "https://quotes.toscrape.com/page/1"),
    (2, "https://quotes.toscrape.com/page/2"),
    (9, "https://quotes.toscrape.com/page/9"),
    (11, "https://quotes.toscrape.com/page/11")
])
def test_create_url_of_page_number(url_creator, page_number, expected):
    """
    This function tests the create_url_of_page_number function in PageURLCreater.
    For all the given page numbers, result of function must be match with expected.
    """
    assert url_creator.create_url_of_page_number(page_number) == expected, "URL should match with expected"