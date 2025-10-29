"""
This program will check if
the extracting data process of the QuoteScraper.extract_data method
works correctly.
"""

from bs4 import BeautifulSoup
import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper import QuoteScraper, Quote, PageURLCreator

@pytest.fixture
def scraper():
    """Return a scraper"""
    return QuoteScraper(PageURLCreator("nomatter"))

@pytest.mark.parametrize("element, text, author, tags",
[
    ("<div><span class='text'>text1</span><small class='author'>author1</small><a class='tag'>tag1</a></div>", "text1", "author1", ["tag1"]),
    ("<div><span class='text'>text2</span><small class='author'>author2</small><a class='tag'>tag-1</a><a class='tag'>tag2</a></div>", "text2", "author2", ["tag-1", "tag2"]),
    ("<div><span class='text'>text3</span><small class='author'>author3</small><a class='tag'>tag0</a></div>", "text3", "author3", ["tag0"]),
    ("<div><span class='text'>text4</span><small class='author'>author4</small><a class='tag'>tagabc</a></div>", "text4", "author4", ["tagabc"]),
    ("<div><span class='text'>text5</span><small class='author'>author5</small><a class='tag'>tag2</a></div>", "text5", "author5", ["tag2"]),
    ("<div><span class='text'>text6</span><small class='author'>author6</small><a class='tag'>tag5</a></div>", "text6", "author6", ["tag5"]),
    ("<div><span class='text'>text7</span><small class='author'>author7</small><a class='tag'>tag-2</a></div>", "text7", "author7", ["tag-2"]),
    ("<div><span class='text'>text8</span><small class='author'>author8</small><a class='tag'>tag-3</a></div>", "text8", "author8", ["tag-3"]),
    ("<div><span class='text'>text9</span><small class='author'>author9</small><a class='tag'>tag-4</a></div>", "text9", "author9", ["tag-4"]),
    ("<div><span class='text'>text10</span><small class='author'>author11</small><a class='tag'>tag-5</a></div>", "text10", "author11", ["tag-5"])
])
def test_all_quote_data_valid(scraper, element, text, author, tags):
    """Check the function for valid elements"""
    tag = BeautifulSoup(element, "html.parser") # Parse the element

    result = scraper.extract_data(tag)

    assert result.text == text, "Text should be equal to text"
    assert result.author == author, "Author should be equal to author"
    assert result.tags == tags, "Tags should be equal to tags"
