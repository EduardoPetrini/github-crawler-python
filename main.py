import requests
import os
import subprocess

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPOS_FOLDER = "repos"

# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub personal access token
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

# GitHub API endpoint for repository search
search_endpoint = 'https://api.github.com/search/repositories'

# Search query parameters
query_params = {
    'q': 'vscode-extension language:JavaScript',  # Search for JavaScript repositories with "vscode-extension" in the name, description, or readme
    'sort': 'stars',  # Sort by stars (ranking)
    'order': 'desc'   # Sort in descending order
}

response = requests.get(search_endpoint, params=query_params, headers=headers)


if not os.path.exists(REPOS_FOLDER):
    os.makedirs(REPOS_FOLDER)

if response.status_code == 200:
    data = response.json()
    for item in data['items']:
        print(f"Repository: {item['name']}")
        print(f"Description: {item['description']}")
        print(f"Stars: {item['stargazers_count']}")
        print(f"URL: {item['html_url']}")
        subprocess.run(f"git clone {item['html_url']} {REPOS_FOLDER}/{item['name']}")
        print("-" * 40)

else:
    print('Request failed with status code:', response.status_code)
    print('Error message:', response.text)
