#!/usr/bin/python3
"""A python script that takes in a URL and an email
address, sends a POST request to the passed URL"""

if __name__ == "__main__":
    from sys import argv
    import requests

    email_address = argv[2]
    url = argv[1]

    payload = {'email': email_address}
    res = requests.post(url, data=payload)

    # Print the body of the response
    print(res.text)
