"""
Tests if a Quote object raises error when invalid attrrşbutes value
given.
"""
import pytest
import sys
import os

# Parent directory'yi path'e ekle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import Quote, QuoteValueInvalidException  # Quote class'ını import et


@pytest.mark.parametrize("text, author, tags",
[
("Some text", "Albert Einstein", ["love"]),
("Another quote text", "Marliyn Monroe", ["science", "bio"]),
("Some other quote", "Albert Einstein",  ["brain", "physics", "money"])
])
def test_all_parameters_given(text, author, tags):
    """
    In this case, all parameters are given and they are all valid.
    """
    quote = Quote(text=text, author=author, tags=tags)

    assert quote.text == text, "Quote text should be equal to the text"
    assert quote.author == author, "Quote author should be equal to author"
    assert quote.tags == tags, "Quote tags should be equal to tags"


@pytest.mark.parametrize("text, author",
[
    ("Some quote text", "Einstein"),
    ("Another quote text", "Darwin")
])
def test_tag_attibute_missing(text, author):
    """
    In this case, the tags list is empty. This should not be a problem.
    The tag list should be an empty list initially.
    """
    quote = Quote(text=text, author=author)

    assert quote.tags == [], "Default tags object should be an empty list."

@pytest.mark.parametrize("text, author, tags",
[
    (None, "Albert Einstein", ["love"]),
    ("Another text", "Tesla", None),
    ("One more text", None, ["luck"]),
    (None, None, ["nothing-is-important"]),
    (None, None, None),
    ("Quote text", None, ["hello", "these", "are", "tags"]),
    (None, "Author without quote", ["notag", "anytag"])
])
def test_none_attribute(text, author, tags):
    """
    In this case, we will make at least one of the attributes None.
    All cases should raise a QuoteValueInvalidException.
    """
    with pytest.raises(QuoteValueInvalidException):
        Quote(text=text, author=author, tags=tags)

@pytest.mark.parametrize("text, author, tags",
[
    ("", "", ["tag1", "tag2", "tag3", "tag4"]),
    ("", "author", ["tag1", "tag2", "tag3"]),
    ("Some fancy quote", "", ["tag1", "tag2", "tag3"]),
    ("      ", "author1", []),
    ("Quote1", "     ", ["tag1", "tag2"])
])
def test_empty_author_or_text(text, author, tags):
    """
    In this case, the length of author attribute or quote attribute will be
    just an empty string or a string with just blanks. This is not acceptable, shoul raise an error.
    """
    with pytest.raises(QuoteValueInvalidException, match="Text or author has a length of zero."):
        Quote(text=text, author=author, tags=tags)

@pytest.mark.parametrize("author, tags",
[
    ("author1", ["tag1", "tag2"]),
])
def test_missing_text(author, tags):
    """
    In this case, the text attribute is not given.
    Should raise an error.
    """
    with pytest.raises(QuoteValueInvalidException, match="Text attribute is None"):
        Quote(author=author, tags=tags)

@pytest.mark.parametrize("text, tags",
[
    ("quote1", ["tag1", "tag2"]),
    ("quote2", ["tag3", "tag4"])
])
def test_missing_author(text, tags):
    """
    In this case, author attribute is missing.
    Should raise an error.
    """
    with pytest.raises(QuoteValueInvalidException, match="Author attribute is None"):
        Quote(text=text, tags=tags)
