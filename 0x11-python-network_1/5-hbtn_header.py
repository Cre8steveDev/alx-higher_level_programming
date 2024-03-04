#!/usr/bin/python3
""" Python Script """

from sys import argv
import requests
"""Write a Python Script that takes in a URL, sends a request to the URL and displays the """

# Make request to the url
res = requests.get(argv[1])
req_id = res.headers["X-Request-Id"]
print(req_id)
