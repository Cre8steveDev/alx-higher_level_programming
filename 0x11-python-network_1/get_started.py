#!/usr/bin/python3
"""Write a Python Script that fetches a response from a given url
https://alx-intranet.hbtn.io/status"""

from urllib import request
import requests

# This returns a Request object to req
req = requests.get("https://www.nairaland.com")
print(req.text)

# r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')

# Read the content of the response object using req.text | req.content | req.json()
# check the encoding with req.encoding and change it with same

# Raw Response Content with open(filename, 'wb') as fd: for chunk in r.iter_content(chunk_size=128): fd.write(chunk)
# Using Response.iter_content will handle a lot of what you would otherwise have to handle when using Response.raw
# directly. When streaming a download, the above is the preferred and recommended way to retrieve the content. Note
# that chunk_size can be freely adjusted to a number that may better fit your use cases.

# Custom Headers
# Pass a dictionary of the key: value headers be passed to the keyword argument
# header. This has less priority than others which can overwrite it
