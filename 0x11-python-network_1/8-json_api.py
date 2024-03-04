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
    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    # attempt to convert the body to json
    try:
        body: dict = res.json()
        if body == {}:
            print("No result")
        else:
            print("[{}] {}".format(body.get("id"), body.get("name")))
    except ValueError as e:
        print("Not a valid JSON")
