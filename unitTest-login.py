from urllib.request import urlopen
from urllib.request import HTTPError
import urllib.parse
from urllib.request import Request

loginUrl = 'http://127.0.0.1:8000/login/'

try:
    response = urlopen(loginUrl).read()
    # print(response.status_code)
    # print(response)

    responseString = response.decode("utf-8") 
    print(responseString)


    tokenString = 'csrfmiddlewaretoken'
    tokenPos = responseString.find(tokenString)

    valueString = "value=\""
    valuePos = responseString.find(valueString, tokenPos)
    valueLen = len(valueString)

    payload = {'username' : 'andrei',
              'password' : '00aaa!!!' }

    if tokenPos and valuePos:
        # tokenValuePos = valuePos + valueLen
        # endOfTokenValue = responseString.find("\"", tokenValuePos)
        # tokenValueSubstr = responseString[tokenValuePos : endOfTokenValue]
        # print("AICI", tokenValueSubstr)
        # payload[tokenString] = tokenValueSubstr
  
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = Request(url = loginUrl, data = data)

        responsePost = urlopen(req).read()
        responseString = responsePost.decode("utf-8") 
        print(responseString)

except HTTPError as error:
    # Need to check its an 404, 503, 500, 403 etc.
    print("Status code ", error.code)
    print("Message ", error.reason)



