# import urllib
# import urllib2
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import HTTPError
import urllib.parse
# CONVERSION from Python2 to Python3
# The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error.

import json

url = 'http://127.0.0.1:8000/article/'
# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }

# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# print(response.read())

#  |
# BECOMES
# \ /
from urllib.request import urlopen
response = urlopen(url).read()
# SAME as
# response = urllib.request.urlopen(url).read()
print(response)


json_object = json.loads(response)

for entry in json_object:
    # now song is a dictionary
    for key, value in entry.items():
        print(key, value) # example usage
    
    print('\n')



# payload = b"{'title' : 'Title', 'author' : 'Andreea', 'email' : 'andreea@gmail.com' }"
payload = {'title' : 'Title',
          'author' : 'Andreea',
          'email' : 'andreea@gmail.com' }
data = urllib.parse.urlencode(payload).encode("utf-8")
req = Request(url = url, data = data)

try:
    response = urlopen(req).read()
    print(response.status_code)
except HTTPError as error:
    # Need to check its an 404, 503, 500, 403 etc.
    print("Status code ", error.code)
    print("Message ", error.reason)
