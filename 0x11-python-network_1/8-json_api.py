#!/usr/bin/python3
"""Write a python script that takes in a letter and sends
a POST request to localhost:5000/search_user with the
letter as a parameter"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from json import JSONDecodeError

    search = "" if len(argv) < 2 else argv[1]
    payload = {"q": search}

    # Make request to the url
    res = requests.post("http://0.0.0.0:5000/search_user", params=payload)

    # attempt to convert the body to json
    try:
        body = res.json()
        if len(body) == 0:
            print("No result")
        else:
            print("[{}] {}".format(body.id, body.name))
    except ValueError as e:
        print("Not a valid JSON")
