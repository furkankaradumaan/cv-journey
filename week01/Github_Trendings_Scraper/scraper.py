'''
This file implements a scraper class
to scrape GithubRepo values from page 'https://github.com/trending'.
'''

from repo import GithubRepo # For GithubRepo object.
import requests
from bs4 import BeautifulSoup, Tag

class RepoScraper:
    '''
    Scrapes github repo information from
    page 'https://github.com/trending'
    '''
    _url = 'https://github.com/trending' # Class variable

    def scrape_page(self) -> set[GithubRepo]:
        '''
        Scrapes all the repos in the url.
        '''
        extracted = set() # Save all repos in a set
        
        soup = self._fetch_page_data()
        if soup is not None:
            # All repositories are represented in div tags with class name 'Box-row'
            # Find all divs.
            repository_divs = soup.find_all('div', class_='Box-row')
            for repository_div in repository_divs:
                repo = self._extract_repo(repository_div) # Extract repository from div element.
                if repo is not None:
                    extracted.add(repo) # Add to set if repo is not None.
        return extracted

    def _fetch_page_data(self) -> BeautifulSoup | None:
        '''
        Fetchs the page data from the url.
        Returns a BeautifulSoup object.
        If request failes returns None.
        '''
        response = requests.get(RepoScraper._url)
        if response.status_code != 200:
            return None # Request failed
        # Request successfull, create a BeautifulSoup object and return it.
        return BeautifulSoup(response.content, 'html.parser')

    def _extract_repo(self, web_element: Tag) -> GithubRepo | None:
        '''
        Extracts the GithubRepo information from given web_element.
        If GithubRepo object runs successfully, returns the GithubRepo
        object, otherwise returns None.
        '''
        # owner username and repository name is in the 'a' tag with class
        # 'Link'.
        a_tag = web_element.find('a', class_='Link')
        if a_tag is None:
            return None # There is no owner name and no repo name.
        owner = self._extract_owner(a_tag)
        repo_name = self._extract_repo_name(a_tag)
        
        # The description is in the first 'p' element.
        p_element = web_element.find('p', class_='col-9')
        if p_element is not None:
            description = self._extract_description(p_element)
        else:
            description = '' # Description is empty string by default.
        
        # Language, stars, and forks information is in the div tag -
        # with class 'f6'.
        div_tag = web_element.find('div', class_='f6')
        if div_tag is None:
            return None

        language = self._extract_language(div_tag)
        stars = self._extract_stars(div_tag)
        forks = self._extract_forks(div_tag)
        
        return GithubRepo(owner,
                          repo_name,
                          description,
                          language,
                          stars,
                          forks
                          )

    def _extract_owner(self, web_element: Tag) -> str | None:
        '''
        Extracts the owner username from web_element.
        If it is not found, returns None.
        '''
        # owner name is in the span tag
        span_tag = web_element.find('span')
        if span_tag is None:
            return None
        owner = span_tag.get_text()
        if owner is None:
            return None

        owner = owner.strip() # Remove leading and trailing spaces
        space_index = owner.find(' ')
        if space_index == -1: # No spaces
            return owner
        return owner[:space_index] # Take the part before space

    def _extract_repo_name(self, web_element: Tag) -> str | None:
        '''
        Extracts the repository name, if it is not found returns None.
        '''
        # repository name is the text of a_tag
        repo_name = web_element.get_text()
        if repo_name is None:
            return None
        repo_name = repo_name.strip()
        space_index = repo_name.rfind(' ')
        if space_index == -1:
            return repo_name
        return repo_name[space_index+1: ]

    def _extract_description(self, web_element: Tag) -> str | None:
        '''
        Extracts the repo description, if no description returns None.
        '''
        # Description is text of p
        description = web_element.get_text()
        if description is None:
            return None
        return description.strip()
    
    def _extract_language(self, web_element: Tag) -> str | None:
        '''
        Extracts the programming language heavily used, if couldnot found,
        returns None.
        '''
        # Language is in the span tag with class 'programmingLanguage'.
        span_tag = web_element.find('span', itemprop='programmingLanguage')
        if span_tag is None:
            return None
        language = span_tag.get_text()
        if language is None:
            return None
        return language.strip()

    def _extract_stars(self, web_element: Tag) -> int | None:
        '''
        Extracts the stars, if couldnot found returns None.
        '''
        # Stars information is in the first 'a' tag with class 'Link'
        a_tag = web_element.find('a', class_='Link')
        if a_tag is None:
            return None
        stars = a_tag.get_text()
        if stars is None:
            return None
        stars = int(stars.replace(',', '')) # Replace the comma with period and convert to int.

        return stars

    def _extract_forks(self, web_element: Tag) -> int | None:
        '''
        Extracts the forks, if could not found returns None.
        '''
        # Forks information is in the second 'a' tag with class = 'Link'
        first_a_tag = web_element.find('a', class_='Link')
        if first_a_tag is None:
            print("First tag None")
            return None
        # Second a tag is the next sibling of this
        second_a_tag = first_a_tag.find_next_sibling('a')
        if second_a_tag is None:
            print("Second tag None")
            return None
        forks = second_a_tag.get_text()
        if forks is None:
            print("Text None")
            return None
        forks = int(forks.replace(',', ''))
        return forks
