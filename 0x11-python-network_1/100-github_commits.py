#!/usr/bin/python3
"""Write a Python script that takes 2 arguments in order to query \
the GitHub API and listst 10 commits from recent to oldest"""

if __name__ == "__main__":
    from sys import argv
    import requests

    repo_name = argv[1]
    owner_name = argv[2]
    header = {"accept": "application/vnd.github+json"}
    query_param = {"per_page": 10, "page": 1}

    github_url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name,)

    res = requests.get(github_url, params=query_param, headers=header)
    data = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                data[i].get("sha"),
                data[i].get("commit").get("author").get("name")))
    except IndexError:
        pass




