'''
This is the main file of scraper program.
'''

from repo import GithubRepo
from scraper import RepoScraper
from repo_analyzer import RepoAnalyzer
from repo_writer import RepoWriter

def main():
    '''
    This file creates a RepoScraper object.
    Then scrape all the repositories in the url
    represented in RepoScraper class.
    Then analysis the results and saves the information into file
    using RepoWriter.
    '''

    scraper = RepoScraper()
    result = scraper.scrape_page()
    analyzer = RepoAnalyzer(result)
    
    RepoWriter.save_to_JSON('repositories.json', result)

    print("==== ANALYSIS ====")
    
    total_repos = analyzer.count()
    print(f"Totally {total_repos} repositories found.")
    
    if total_repos == 0:
        print("No repositories to analyze")
        return

    most_starred_repo = analyzer.most_starred_n(1).get().iloc[0]
    print(f"Most starred repository: ")
    print(f"Owner          : {most_starred_repo['owner']}")
    print(f"Repository Name: {most_starred_repo['repo_name']}")
    print(f"Description    : {most_starred_repo['description']}")
    print(f"Language       : {most_starred_repo['language']}")
    print(f"Stars          : {most_starred_repo['stars']}")
    print(f"Forks          : {most_starred_repo['forks']}")

if __name__ == '__main__':
    main()
