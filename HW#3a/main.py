import json
import requests

def get_commits(id: str, repo: str):
    '''
    Gets the number of commits of a specific repo

    Args: 
        id (str): id of github user
        repo (str): string containing name of repo
        
    Returns:
        commits (int): number of commits on repo owned by id
    '''
    if id == None or not isinstance(id, str):
        return 0

    if repo == None or not isinstance(repo, str):
        return 0
    
    response = requests.get(f'https://api.github.com/repos/{id}/{repo}/commits')
    response_dict = response.json()
    if isinstance(response_dict, dict) and response_dict['message'] == 'Not Found':
        return 0

    commits = len(response_dict)
    return commits

def get_repos(id:str):
    '''
    Gets the name of the repos owned by a user

    Args:
        id (str): id of github user
    Returns:
        repos (list): number of repos owned by the user
    '''
    if id == None or not isinstance(id, str):
        return []
    
    response = requests.get(f'https://api.github.com/users/{id}/repos')
    response_dict = response.json()

    if isinstance(response_dict, dict) and response_dict['message'] == 'Not Found':
        return []
    
    repos = [response_dict[i]['name'] for i in range(len(response_dict))]
    return repos

def get_repos_and_commits(id:str):
    repos = get_repos(id)
    repo_commits = [f'Repo: {repos[i]} Number of Commits: {get_commits(id, repos[i])}' for i in range(len(repos))]
    return repo_commits

if __name__ == '__main__':
    id = 'richkempinski'
    lines = get_repos_and_commits(id)
    for i in lines:
        print(i)