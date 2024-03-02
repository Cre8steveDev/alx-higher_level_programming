#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

# Prepare the Request object
req = urllib.request.Request("https://alx-intranet.hbtn.io/status")

# Pass in the request object to the urlopen within a context
with urllib.request.urlopen(req) as res:
    response = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8: {}".format(response.decode("utf-8")))
