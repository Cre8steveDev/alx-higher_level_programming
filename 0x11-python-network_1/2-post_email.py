#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    # Get url and email from Command line
    url = argv[1]
    data = urlencode({"email": argv[2]}).encode("ascii")

    # create Request object
    req = Request(url, data)

    with urlopen(req) as response:
        """Open the url with the data to get a response"""
        print(response.read().decode("utf-8"))
