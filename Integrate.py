import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
github_token   = os.getenv('github_token')
github_base_url = os.getenv('github_base_url')
headers = {'Authorization': f'token {github_token }'}

def get_repositories_name(username, github_base_url="https://api.github.com/users", token=""):
    headers = {'Authorization': f'token {token}'} if token else {}
    repos_url = f"{github_base_url}/{username}/repos"
    try:
        response = requests.get(repos_url, headers=headers)
        response.raise_for_status()
        return [repo['name'] for repo in response.json()]
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving repository names: {e}")
        return []

def get_branches_name(username, repo):
    branches_url = f"{github_base_url}/{username}/{repo}/branches"
    try:
        response = requests.get(branches_url, headers=headers)
        response.raise_for_status()
        return [branch['name'] for branch in response.json()]
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving branch names: {e}")
        return []

def get_github_data(username, repo, branch):
    base_url = f"https://api.github.com/repos/{username}/{repo}"    
    data = {        
        # 'Branches name': get_branches_name(username, repo),
        'Branch': get_branch_data(base_url, branch),
        'Commits': get_commits(base_url, branch),
        'Commit Comments': get_commit_comments(base_url, branch),
        'Collaborators': get_collaborators(base_url)
    }
    return(json.dumps(data, indent=4))

def get_branch_data(base_url, branch):
    branch_url = f"{base_url}/branches/{branch}"
    try:
        response = requests.get(branch_url, headers=headers)
        response.raise_for_status()
        branch_data = response.json()
        return {
            "name": branch_data['name'],
            "commit": branch_data['commit']['sha']
        }
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving branch data: {e}")
        return {}
    
def get_commits(base_url, branch):
    commits_url = f"{base_url}/commits?sha={branch}"
    try:
        response = requests.get(commits_url, headers=headers)
        response.raise_for_status()
        commits = [prepare_commit_data(commit) for commit in response.json()]
        return commits
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving commits: {e}")
        return []
    
def prepare_commit_data(commit):
    return      {"url": commit['url'],
                "comments_url": commit['comments_url'],
                "commit": {
                    "url": commit['html_url'],
                    "author": {
                        "name": commit['commit']['author']['name'],
                        "email": commit['commit']['author']['email'],
                        "date": commit['commit']['author']['date']
                    },
                    "committer": {
                        "name": commit['commit']['committer']['name'],
                        "email": commit['commit']['committer']['email'],
                        "date": commit['commit']['committer']['date']
                    },
                    "message": commit['commit']['message'],
                    "comment_count": commit['commit']['comment_count']
                }}

def get_commit_comments(base_url, branch):
    commits = get_commits(base_url, branch)
    all_comments = []
    for commit in commits:
        comments_url = commit['comments_url']
        try:
            response = requests.get(comments_url, headers=headers)
            response.raise_for_status()
            comments = response.json()
            for comment in comments:
                all_comments.append({
                    "commit_id": comment['commit_id'],
                    "user": comment['user'],
                    "body": comment['body']
                })
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving comments for commit: {e}")
    return all_comments

def get_collaborators(base_url):
    collaborators_url = f"{base_url}/collaborators"
    try:
        response = requests.get(collaborators_url, headers=headers)
        return [{"login": collaborator['login'], "role_name": collaborator['role_name']} for collaborator in response.json()]
    except requests.exceptions.RequestException as e:
            print(f"Error retrieving comments for commit: {e}")
            return []
    
if __name__ == "__main__":
    username = "AhmadDerieh1"

    repository_data = []
    repositories = get_repositories_name(username,token=github_token)

    data={} 
    for repository in repositories:
        branches = get_branches_name(username, repository)
        for branch in branches:
            branch_data = get_github_data(username, repository, branch).strip()
            branch_data_clean = branch_data.replace("\n", "").replace("    ", " ")  # Remove newlines and reduce indentation
            repository_data.append(branch_data_clean)
        data[repository]= repository_data

    json_string = json.dumps(data, indent=4)

    with open('my_dict.txt', 'w') as file:
        file.write(json_string)