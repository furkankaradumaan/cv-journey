"""
This files purpose is to test the GithubRepo dataclass in
the file repo.py.
"""

import sys, os
# We will add the path of the parent directory, so
# we can include repo.py file.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from repo import GithubRepo, InvalidAttributeError

import pytest # Test framework


@pytest.mark.parametrize("owner, repo_name, description, language, stars, forks",
                         [
                            ("furkan", "repo", "repo desc", "Python", 11, 10),
                            ("fatih", "repo2", "description", "Java", 0, 1),
                            ("yasir", "notebook", "nodesc", "C++", 0, 0),
                            ("talha", "homework", "", "", 1, 0),
                            ("gürkan", "atm-machine", "useful ATM", "C", 100, 20),
                            ("betül", "barbie-home", "I love barbie", "", 18, 7),
                            ("username", "a", "desc", "Ruby", 0, 0),
                             ])
def test_repo_creation_successfull(owner, repo_name, description,
                                   language, stars, forks):
    """
    This function checks the creation process with valid arguments.
    We expect that all the cases the object is created successfully and
    the values of the attributes of the instance variable are matches.
    """
    repo = GithubRepo(owner, repo_name, description, language, stars, forks)
    
    assert repo.owner == owner, "Owner name is wrong"
    assert repo.repo_name == repo_name, "Repo name is wrong"
    assert repo.description == description, "Description is wrong"
    assert repo.language == language, "Language is wrong"
    assert repo.stars == stars, "Stars is wrong"
    assert repo.forks == forks, "Shares is wrong"


@pytest.mark.parametrize("owner, repo_name, description, language, stars, forks",
                         [
                            ("", "repo_name", "repo_desc", "Python", 10, 11), # Username has a length of 0, invalid.
                            (None, "firstrepo", "first project", "Java", 1, 5), # Username is None, invalid.
                            ("furkan", "", "my project", "Rust", 3, 6), # Repository name has a length of 0, invalid.
                            ("fatih", None, "description", "TypeScript", 5, 9), # Repository name is None, invalid.
                            ("emir", "ATM", None, "C#", 1, 0), # Description is None, invalid.
                            ("betül", "barbie", "description", None, 4, 6), # Language is None, invalid.
                            ("eren", "cproject", "desc", "C++", -2, 4), # Stars negative, invalid.
                            ("tarık", "atm", "desc", "Java", 4, -1), # Shares negative, invalid.
                            (120, "atm", "desc", "Java", 12, 12), # Username is not a string, invalid.
                            ("furkan", True, "desc", "Python", 0, 1), # Repo name is not a string, invalid.
                            ("deniz", "atm", 10, "C#", 4, 1), # Description is not a string, invalid.
                            ("korhan", "pswman", "desc", dict(), 0, 0), # Language is not a string, invalid.
                            ("furkan", "webapp", "flask", "Python", 120.40, 20), # Stars is not int, invalid.
                            ("linus", "kernel", "UNIX-based", "C", 20, 10.33), # Shares is not int, invalid.
                             ])
def test_repo_creation_failed(owner, repo_name, description,
                              language, stars, forks):
    """
    This function checks the creation process with invalid arguments.
    In all cases we should get an error.
    """
    with pytest.raises(InvalidAttributeError):
        repo = GithubRepo(owner, repo_name, description, language, stars, forks)


@pytest.mark.parametrize("owner, repo_name, description, language, stars, forks",
                         [
                            ("furkan", "repo", "desc", "Python", 0, 0),
                            ("betül", "barbie", "love barbie", "", 1, 1),
                            ("talha", "yeni-şarkı", "spotify'da", "", 100, 120),
                            ("gürkan", "file-manager", "C file manager", "C", 200, 1000),
                             ])
def test_to_dictionary(owner, repo_name, description,
                        language, stars, forks):
    
    attr_names = [
                    "owner",
                    "repo_name",
                    "description",
                    "language",
                    "stars",
                    "forks",
                  ]
    values = [
                owner,
                repo_name,
                description,
                language,
                stars,
                forks,
                ]

    expected = {key:value for key, value in zip(attr_names, values)}

    repo = GithubRepo(*values)
    dict_ = repo.to_dict()

    assert dict_ == expected
