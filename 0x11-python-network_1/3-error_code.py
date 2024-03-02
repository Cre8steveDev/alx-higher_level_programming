#!/usr/bin/python3
"""Write a python script that takes in a URL, sends a
request to the URL and displays the body of the response
decoded in utf-8 while handling error"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    # create Request object
    req = Request(argv[1])

    try:
        with urlopen(req) as response:
            """Open the url with the data to get a response"""
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.status))
