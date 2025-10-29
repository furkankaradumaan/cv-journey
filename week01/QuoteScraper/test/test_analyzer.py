"""
Tests the QuoteAnalyzer class.
"""

import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scraper import Quote, QuoteAnalyzer
import pandas as pd

@pytest.mark.parametrize("input, expected, min_length, negate",
[
    [
        [
            Quote("some_text for mock quote", "author1"), 
            Quote("some mock text for", "author2"),
            Quote("text", "author1"), 
            Quote("another text", "author")
        ],
        [
            Quote("some_text for mock quote", "author1"), 
            Quote("some mock text for", "author2")
        ],
        13,
        False
    ],
    [
        [
            Quote("text for quote", "author"),
            Quote("I am twenty years old", "author"),
            Quote("Hello, everyone! My name is", "author"),
            Quote("Some short text", "author"),
            Quote("just text", "author"),
            Quote("What are you doing bro! Are you OK?", "author")
        ],
        [
            Quote("I am twenty years old", "author"),
            Quote("Hello, everyone! My name is", "author"),
            Quote("What are you doing bro! Are you OK?", "author")
        ],
        20,
        False
    ],
    [
        [
            Quote("My name is Furkan Karaduman", "author"),
            Quote("I live in Istanbul", "author"),
            Quote("I am a student at Istanbul University", "author")
        ],
        [
            Quote("I live in Istanbul", "author") 
        ],
        20,
        True
    ],
    [
        [
            Quote("I love playing football, do you?", "author"),
            Quote("Or you like tennis?", "author"),
            Quote("Do you think Messi is an alien?", "author"),
            Quote("How is it going bro?", "author"),
            Quote("Hello, how are you?", "author"),
            Quote("My name is Furkan", "author")
        ],
        [
            Quote("My name is Furkan", "author")
        ],
        18,
        True
    ]
])
def test_minimum_length(input, expected, min_length, negate):
    """
    This function tests the minimum_length_function
    """

    # Create a QuoteAnalyzer instance
    analyzer = QuoteAnalyzer(input)

    filtered_data = analyzer.minimum_length(min_length, negate).get()
    filtered_data = filtered_data.reset_index(drop=True)

    expected_df = pd.DataFrame(
        {
            "text": [quote.text for quote in expected],
            "author": [quote.author for quote in expected],
            "tags": [quote.tags for quote in expected]
        }
    )
    expected_df = expected_df.reset_index(drop=True)
    assert filtered_data.equals(expected_df)
    
