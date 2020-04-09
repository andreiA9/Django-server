from urllib.request import urlopen
from urllib.request import Request
from urllib.error import HTTPError
import urllib.parse
# CONVERSION from Python2 to Python3
# The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error.

import json

# trebuie neaparat LINK ul de API
# url = 'http://127.0.0.1:8000/article/'
url = 'http://127.0.0.1:8000/api/v1/article/'


def httpGet():
    # GET
    response = urlopen(url).read()

    responseString = response.decode("utf-8") 
    print(responseString)

    return responseString

def printJsonResponse(responseString):
    json_object = json.loads(responseString)

    for entry in json_object:
        # now song is a dictionary
        for key, value in entry.items():
            print(key, value) # example usage
        
        print('\n')

def httpPost(payload):
    # PREPARE payload for POST
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = Request(url = url, data = data)

    # POST
    responsePost = urlopen(req).read()
    responseString = responsePost.decode("utf-8") 
    print(responseString)

if __name__ == "__main__":
    # not needed
    # setupHttpHandler()

    responseString = httpGet()

    printJsonResponse(responseString)

    # payload = b"{'title' : 'Title', 'author' : 'Andreea', 'email' : 'andreea@gmail.com' }"
    payload = {'title' : 'Title',
            'author' : 'Andreea',
            'email' : 'andreea@gmail.com' }

    try:
        httpPost(payload)

    except HTTPError as error:
        print("Status code ", error.code)
        print("Message ", error.reason)

# OUTPUT
# the inserted-ELEMENT in JSON
# b'{"id":12,"title":"Title","author":"Andreea","email":"andreea@gmail.com","date":"2020-04-06T05:47:52.097335Z"}'