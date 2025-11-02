'''
Includes pytest fixtures for test_scraper.py file.
'''

from bs4 import BeautifulSoup
import pytest

@pytest.fixture(scope='session',
                params=[
                    # Owner extaction cases
                    {'username': 'username /',                     'expected': 'username',               "type": "owner"},
                    {'username': '  furkan  /',                    'expected': 'furkan',                 "type": "owner"},
                    {'username': 'get-conv /',                     'expected': 'get-conv',               "type": "owner"},
                    {'username': '',                               'expected': '',                       "type": "owner"},
                    {'username': 'my-username  / hello',           'expected': 'my-username',            "type": "owner"},
                    # repo_name extraction cases
                    {'repo_name': 'repo',                          'expected': 'repo',                   "type": "repo_name"},
                    {'repo_name': '  rep',                         'expected': 'rep',                    "type": "repo_name"},
                    {'repo_name': 'us / rep ',                     'expected': 'rep',                    "type": "repo_name"},
                    # description extraction cases
                    {'description': '   This is a description   ', 'expected': 'This is a description',  "type": "description"},
                    # language cases
                    {'language': 'Python',                         'expected': 'Python',                 "type": "language"},
                    {'language': '   Java  ',                      'expected': 'Java',                   "type": "language"},
                    # stars cases
                    {'stars': '  12,191  ',                        'expected': 12191,                    "type": "stars"},
                    {'stars': '  123',                             'expected': 123,                      "type": "stars"},
                    {'stars': '0  ',                               'expected': 0,                        "type": "stars"},
                    {'stars': '1,123,120',                         'expected': 1123120,                  'type': "stars"},
                    # forks cases
                    {'forks': '   1000  ',                         'expected': 1000,                     'type': 'forks'},
                    {'forks': '1,121,131,131',                     'expected': 1121131131,               'type': 'forks'}
                    ]
                )
def web_element(request):
    
    expected = request.param['expected']
    test_type = request.param['type']
    
    if test_type == 'owner':
        username = request.param['username'] # Get current parameter name.
        html_tag = f"<a class='Link'> <span class='normal-text'>{username}</span></a>"
    elif test_type == 'repo_name':
        repo_name = request.param['repo_name']
        html_tag = f"<a class='Link'><span> username </span>{repo_name}</a>"
    elif test_type == 'description':
        description = request.param['description']
        html_tag = f"<p>{description}</p>"
    elif test_type == 'language':
        language = request.param['language']
        html_tag = f"<div class='f6'><span><span></span><span itemprop='programmingLanguage'>{language}</span></span></div>"
    elif test_type == 'stars':
        stars = request.param['stars']
        html_tag = f"<div class='f6'><span><span></span><span></span></span><a class='Link'>{stars}</a></div>"
    elif test_type == 'forks':
        forks = request.param['forks']
        html_tag = f"<div class='f6'><span><span></span><span></span></span><a class='Link'></a><a class='Link'>{forks}</a></div>"

    soup = BeautifulSoup(html_tag, 'html.parser')
    return {'tag': soup, 'expected': expected, "type": test_type}
