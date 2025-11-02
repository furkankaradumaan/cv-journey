'''
This file tests RepoAnalyzer class.
'''

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper import GithubRepo
from repo_analyzer import RepoAnalyzer
import json # To load sample repository data.

import pytest

@pytest.fixture(scope="session")
def sample_repo_data():
    '''
    this function loads the sample repository data
    in the file analyzer_sample_repo.json.
    Returns the dictionary object.
    '''
    json_name = "analyzer_sample_repo.json"
    repo_data = None
    with open(json_name, "r", encoding="utf-8") as json_file:
        repo_data = json.load(json_file)

    return repo_data

@pytest.fixture(scope="session")
def test_cases(sample_repo_data):
    '''
    This function gets the sample repository data
    from sample_repo_data.
    After getting the test_cases data, it will create
    a new result list with suitable dictionaries in repos.
    '''
    # Get all the test cases.
    tests = sample_repo_data['test_cases'].items()

    # Loop through each test.
    for test_key, test in tests:
        # Get the result set.
        expected_result = test['result']
        expected_result_updated = set()
        # For each element in expected result
        # Get the suitable repository dict from sample_repo_data['repos']
        # and add it form into a new set.
        for repo_key in expected_result:
            # Get the repository
            repo_dict = sample_repo_data['repos'][repo_key]
            repo_obj = GithubRepo(
                    repo_dict['owner'],
                    repo_dict['repo_name'],
                    repo_dict['description'],
                    repo_dict['language'],
                    repo_dict['stars'],
                    repo_dict['forks']
                    )
            expected_result_updated.add(repo_obj)
        # Update the expected result.
        sample_repo_data['test_cases'][test_key]['result'] = expected_result_updated 
    
    return sample_repo_data["test_cases"]

@pytest.fixture(scope='session')
def sample_repos(sample_repo_data):
    '''
    Gets the sample repository data from sample_repo_data.
    Converts the elements in dictionary to GtihubRepo objects.
    Returns the repos in a set.
    '''
    repos = set()
    
    for repo_key, repo_dict in sample_repo_data['repos'].items():
        repo = GithubRepo(
                owner       = repo_dict['owner'],
                repo_name   = repo_dict['repo_name'],
                language    = repo_dict['language'],
                description = repo_dict['description'],
                stars       = repo_dict['stars'],
                forks       = repo_dict['forks']
                )
        
        repos.add(repo)
    
    return repos

@pytest.fixture(scope='function')
def analyzer(sample_repos):
    '''
    Returns a sample RepoAnalyzer object.
    '''
    return RepoAnalyzer(sample_repos)

    
class TestRepoAnalyzerManager:
    def test_apply_suitable_test(self, analyzer, test_cases):
        '''
        This method loops through each test_case.
        Determines which method to call for each test
        case and calls that test method.
        '''
        for test_key, test_case in test_cases.items():
            test_method = test_case['test_method']
            if test_method == 'minimum_stars':
                self._minimum_stars_test(analyzer, test_case)
            elif test_method == 'maximum_stars':
                pass
                #self._maximum_stars_test(analyzer, test_case) # APPLY
            elif test_method == 'most_starred_n':
                pass
                #self._most_starred_n_test(analyzer, test_case) ## APPLY
            elif test_method == 'minimum_forks':
                pass
                #self._minimum_forks_test(analyzer, test_case) # APPLy
            elif test_method == 'maximum_forks':
                pass
                #self._maximum_forks_test(analyzer, test_case) # APPLY
            elif test_method == 'most_forked_n':
                pass
                #self._most_forked_n_test(analyzer, test_case) # APPLY
            elif test_method == 'with_substring':
                pass
                #self._with_substring_test(analyzer, test_case) # APPLY
            else:
                assert False, ('''
                                This else case should be never exevuted.
                                There must a a fault about the naming of test method types.
                                Check it.
                                ''')
   
    def _minimum_stars_test(self, analyzer, test_case):
        '''
        This function tests minimum_stars method in RepoAnalyzer class.
        '''
        stars = test_case['input']

        assert isinstance(stars, int), ('''
                                        There is a problem with the 'stars' input.
                                        It is not type of integer.
                                        ''')

        result = analyzer.minimum_stars(stars).get()
        
        # The result is type of pandas.DataFrame.
        # We need to convert the result to set of tuples
        # that represent GithubRepo objects.
        list_of_named_tuples = list(result.itertuples(index=False))
        
        # Convert the tuples to GithubRepos
        set_of_repos = set()
        for repo_info in list_of_named_tuples:
            repo = GithubRepo(
                    repo_info.owner,
                    repo_info.repo_name,
                    repo_info.description,
                    repo_info.language,
                    repo_info.stars,
                    repo_info.forks
                    )
            set_of_repos.add(repo)

        # Compare the result with expected result
        assert set_of_repos == test_case['result']


