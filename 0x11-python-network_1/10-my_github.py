#!/usr/bin/python3
"""Write a Python script that takes your github credentials
(username and password - token) and uses the GITHUB API to
display your id"""

if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    username = argv[1]
    passwd = argv[2]

    auth = HTTPBasicAuth(username, passwd)

    res = requests.get("https://api.github.com/user", auth=auth)
    data = res.json()

    print(data.get("id"))
