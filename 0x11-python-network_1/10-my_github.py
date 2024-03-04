#!/usr/bin/python3
"""Write a Python script that takes your github credentials
(username and password - token) and uses the GITHUB API to
display your id"""

if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    username = argv[1]
    password = argv[2]

    auth_ = HTTPBasicAuth(username, password)

    res = requests.get("https://api.github.com/user", auth=auth_)
    data = res.json()
    print(data.get("id"))
