#!/usr/bin/python3
"""
This module sends a request to the GitHub API and displays the 10 most recent
commits of a specified repository.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    response = requests.get(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    )

    commits = response.json()

    for commit in commits[:10]:
        commit_sha = commit.get('sha')
        commit_author_name = commit.get('commit').get('author').get('name')
        print(f"{commit_sha}: {commit_author_name}")
