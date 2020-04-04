# import urllib
# import urllib2
from urllib.request import urlopen
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
print(response)

toJson = json.loads(response)
print(toJson)
print(toJson[0]['title'])
print(toJson[1]['title'])
print(toJson[0]['author'])
print(toJson[1]['author'])


# OUTPUT
# b'[{"title": "Title1", "author": "Andrei", "email": "andrei_andreescu24@yahoo.com", "date": "2020-04-04T01:00:09.446819Z"},
#  {"title": "Title2", "author": "George", "email": "george@yahoo.com", "date": "2020-04-04T01:04:13.394649Z"}]'