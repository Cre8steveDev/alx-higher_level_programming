#!/usr/bin/python3
"""Write a Python Script that takes in a URL,
sends a request to the URL and displays the """

if __name__ == "__main__":
    from sys import argv
    import requests

    # Make request to the url
    res = requests.get(argv[1])
    req_id = res.headers.get("X-Request-Id", None)

    if req_id:
        print(req_id)
