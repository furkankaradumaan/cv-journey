'''
This file tests the Scraper objects methods in scraper.py file.
'''

import random
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper import RepoScraper
import scraper
from repo import GithubRepo
import pytest
from conf_test_scraper import *

@pytest.fixture(scope='function')
def repo_scraper():
    return RepoScraper() # Return new repo_scraper object

def test_repo_scraper_units(web_element, repo_scraper):
    '''
    This function will test the extract_owner method of Scraper
    class for multiple cases. All cases should be completed successfully.
    '''

    element = web_element['tag']
    expected = web_element['expected']
    test_type = web_element['type']
    
    if test_type == 'owner':
        result = repo_scraper._extract_owner(element)
    elif test_type == 'repo_name':
        result = repo_scraper._extract_repo_name(element)
    elif test_type == 'description':
        result = repo_scraper._extract_description(element)
    elif test_type == 'language':
        result = repo_scraper._extract_language(element)
    elif test_type == 'stars':
        result = repo_scraper._extract_stars(element)
    elif test_type == 'forks':
        result = repo_scraper._extract_forks(element)
    else:
        raise ValueError(f"Unknown test type: {test_type}")

    assert result == expected, f"result: '{result}', expected: '{expected}'"


@pytest.mark.parametrize("owner, repo_name, description, language, stars, forks",
                         [
                            ("furkan", "name_of_repo", "rep-desc", "Python", 1211, 100)
                             ])
def test_extract_repo(owner, repo_name, description, language, stars, forks,
                      mocker, repo_scraper):
   
    mock_owner = mocker.patch("scraper.RepoScraper._extract_owner")
    mock_owner.return_value = owner

    mock_repo_name = mocker.patch("scraper.RepoScraper._extract_repo_name")
    mock_repo_name.return_value = repo_name

    mock_description = mocker.patch("scraper.RepoScraper._extract_description")
    mock_description.return_value = description

    mock_language = mocker.patch("scraper.RepoScraper._extract_language")
    mock_language.return_value = language

    mock_stars = mocker.patch("scraper.RepoScraper._extract_stars")
    mock_stars.return_value = stars

    mock_forks = mocker.patch("scraper.RepoScraper._extract_forks")
    mock_forks.return_value = forks
    
    mock_web_element = mocker.patch("scraper.Tag")
    mock_find = mocker.patch("scraper.Tag.find")
    mock_find.return_value = mocker.Mock()
    mock_web_element.find = mock_find

    result = repo_scraper._extract_repo(mock_web_element)

    assert result == GithubRepo(owner, repo_name, description, language, stars, forks)

# The True/False indicator for fetch_data_res means that if the
# value is True, then fetch_page_data mock object will return Mock divs
# same as the length of repos list.
# If it is False, then fetch_page_data mock object will return None.
# 
# For the boolean dictionary, number of True values specifies the
# number of valid repositories, number of False value specifies the
# numebr of None repositories.
@pytest.mark.parametrize("fetch_data_res, repos",
                         [
                            (True,  {'True': 4, 'False': 7}),
                            (True,  {'True': 1, 'False': 8}),
                            (True,  {'True': 0, 'False': 3}),
                            (True,  {'True': 4, 'False': 2}),
                            (False, {'True': 2, 'False': 3}),
                            (True,  {'True':10, 'False': 1}),
                            (True,  {'True': 0, 'False': 0}),
                            (False, {'True': 3, 'False': 4})
                             ])
def test_scrape_page_successfull(fetch_data_res, repos, mocker, repo_scraper):
    
    total_repos = repos['True'] + repos['False']
    # First we need to mock the fetch_data method
    mock_fetch = mocker.patch.object(repo_scraper, '_fetch_page_data') 

    # If fetch data result specified as False, then
    # return type of this mock object should be None.
    if fetch_data_res is False:
        mock_fetch.return_value = None
        
        # Since mock_fetch function will return None, the function should
        # directly return an empty set. So we don't need to mock anything else.
        repos_set = repo_scraper.scrape_page()

        assert repos_set == set()
    else:
        # If it is not, it should return a BeautifulSoup object
        # This soup object must return div tags.
        divs = [mocker.Mock() for _ in range(total_repos)] # number of div tags is same as number of repos.
        mock_soup = mocker.Mock()
        mock_soup.find_all.return_value = divs
        
        mock_fetch.return_value = mock_soup
    
        # We will send every div element into _extract_repo method.
        # We need to mock all the repos and the _extract_repo method.
        mock_extract_repo = mocker.patch.object(repo_scraper, "_extract_repo")

        # The number of valid and invalid repos is specified in repos dictionary.
        invalid_repos = [None for invalid_repo in range(repos['False'])]
        valid_repos = []
        for i in range(repos['True']):
            repo_mock = mocker.Mock()
            repo_mock.name = f"Repo_{i}"
            valid_repos.append(repo_mock)

        # This extract_repo mock object will return the repos one
        # by one in every iteration.
        repos_list = invalid_repos + valid_repos
        random.shuffle(repos_list)
        mock_extract_repo.side_effect = repos_list
        
        # Now we can call scrape_page method
        # The return value is a set of valid repositories.
        repos_set = repo_scraper.scrape_page()
    
        assert repos_set == set(valid_repos)   


