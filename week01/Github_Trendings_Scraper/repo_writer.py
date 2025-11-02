'''
This file implements a RepoWriter class
to write the GithubRepo data into a specified JSON or CSV file.
'''

import json
import csv
from repo import GithubRepo

class RepoWriter:
    '''
    Implements static methods to write
    the repository data to files in multiple formats.
    '''

    @staticmethod
    def save_to_CSV(csv_name, repos: set[GithubRepo]):
        '''
        Save the repositories into a CSV file with given name.
        '''
        with open(csv_name, "w", encoding="utf-8", newline='') as csv_file:
            dict_writer = csv.DictWriter(csv_file, fieldnames=GithubRepo.__slots__)
            
            dict_writer.writeheader()
            for repo in repos:
                dict_writer.writerow(repo.to_dict())


    def save_to_JSON(json_name, repos: set[GithubRepo]):
        '''
        Saves the repositories into a JSON file with given name
        '''
        with open(json_name, 'w', encoding='utf-8') as json_file:
            repos_as_dicts = dict()
            for i, repo in enumerate(repos):
                repo_key = f"repo{i}"
                repos_as_dicts[repo_key] = repo.to_dict()

            json.dump(repos_as_dicts, json_file, indent=4, ensure_ascii=False)
