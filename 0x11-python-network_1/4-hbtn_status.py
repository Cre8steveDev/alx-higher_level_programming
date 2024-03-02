#!/usr/bin/python3
"""Write a Python Script that fetches a url"""

import requests
from requests.exceptions import HTTPError, ConnectionError

try:
    response = requests.get("https://alx-intranet.hbtn.io/status")
    # print(dir(response))
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
except (HTTPError, ConnectionError) as e:
    pass
