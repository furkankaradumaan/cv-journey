'''
This file is designed to analyze trendings repository data.
'''

import pandas as pd
from scraper import GithubRepo

class RepoAnalyzer:
    '''
    This class stores a list of GithubRepo objects with DataFrame.
    Make it possible to analyze and filter the repoistories.
    '''

    def __init__(self, repos: set[GithubRepo]):
        '''
        Accepts a set of GithubRepo, write the data into DataFrame.
        Also creates an additional DataFrame (__filtered) to keep
        the filtered repos.
        '''
        repos_dict = [repo.to_dict() for repo in repos]
        self.df = pd.DataFrame(repos_dict)
            
        self.__filtered = self.df.copy()

    def minimum_stars(self, stars: int) -> 'RepoAnalyzer':
        '''
        Takes the repositories whose stars attribute is at least 'stars'
        Returns self to maintain method chaining.
        '''
        cond = self.__filtered['stars'] >= stars
        self.__filtered = self.__filtered[cond]
        
        return self
    
    def maximum_stars(self, stars: int) -> 'RepoAnalyzer':
        '''
        Takes the repositories whose stars attribute is at most 'stars'.
        Returns self to maintain method chaining.
        '''
        cond = self.__filtered['stars'] <= stars
        self.__filtered = self.__filtered[cond]

        return self
    
    def most_starred_n(self, n: int) -> 'RepoAnalyzer':
        '''
        Takes the n repositories which are most starred.
        Returns self to maintain method chaining.
        '''
        self.__filtered = self.__filtered.nlargest(n, ['stars'])
        return self

    def minimum_forks(self, forks: int) -> 'RepoAnalyzer':
        '''
        Takes the repositories which are forked at least 'forks' times.
        Returns self to maintain method chaining.
        '''
        cond = self.__filtered['forks'] >= forks
        self.__filtered = self.__filtered[cond]
        
        return self
    
    def maximum_forks(self, forks: int) -> 'RepoAnalyzer':
        '''
        Takes the repositories which are forked at most 'forks' times.
        Returns self to maintain method chaining.
        '''
        cond = self.__filtered['forks'] <= forks
        self.__filtered = self.__filtered[cond]

        return self

    def most_forked_n(self, n: int) -> 'RepoAnalyzer':
        '''
        Takes the n repositories with maximum forks.
        Returns self to maintain method chaining.
        '''
        self.__filtered = self.__filtered.nlargest(n, ['forks'])
        return self

    def with_substring(self, substr: str, field) -> 'RepoAnalyzer':
        '''
        Takes the repositories whose usernames contains the
        given substring.
        Returns self to maintain method chaining.
        '''
        if field not in ['owner', 'repo_name', 'description']:
            return self

        cond = self.__filtered[field].str.contains(substr)
        self.__filtered = self.__filtered[cond]
        
        return self
    
    def count(self) -> int:
        '''
        Returns the length of filtered list.
        '''
        return self.__filtered.shape[0]
    
    def get(self) -> pd.DataFrame:
        '''
        Returns a copy of the filtered DataFrame
        '''
        return self.__filtered.copy()

    def clear(self) -> 'RepoAnalyzer':
        '''
        Clears all the filters on filtered dataframe.
        '''
        self.__filtered = self.df.copy()
        return self
