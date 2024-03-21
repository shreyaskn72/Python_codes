import requests

# GitHub API credentials
username = 'your_username'
token = 'your_personal_access_token'  # Generate at https://github.com/settings/tokens

repo_owner = 'username'
repo_name = 'repository'

headers = {
    'Authorization': f'token {token}'
}

response_branches = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/branches', headers=headers)
branches = response_branches.json()

total_size = 0

for branch in branches:
    branch_name = branch['name']
    response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/{branch_name}?recursive=1', headers=headers)
    data = response.json()
    branch_size = sum(int(item['size']) for item in data['tree'] if item['type'] == 'blob')
    total_size += branch_size

print(f"Total size of the repository across all branches: {total_size / (1024 * 1024)} MB")
