import urllib.request
import urllib.response
from urllib.request import HTTPError
# LINIE FOARTE IMPORTANTA
from base64 import b64encode

userName = "andrei"
passWord  = "00aaa!!!"
loginUrl = 'http://127.0.0.1:8000/genericapi/v1/detail/0/'


#we need to base 64 encode it 
#and then decode it to acsii as python 3 stores it as a byte string
credentials = b64encode(b"andrei:00aaa!!!").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  credentials }

request = urllib.request.Request(url = loginUrl, headers = headers)

try:
    response = urllib.request.urlopen(request).read()
    print(response)
except HTTPError as error:
    print("Status code ", error.code)
    print("Message ", error.reason)