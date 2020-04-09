from urllib.request import urlopen
from urllib.request import HTTPError
import urllib.parse
from urllib.request import Request

from urllib.request import install_opener
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor
from urllib.request import HTTPHandler

# COOKIES
from http.cookiejar import CookieJar


""" !!!! INSTRUCTIUNI
vezi in capture - POST.png

pentru login se va proceda in felul urmator:
0 = se face un GET la URL='customlogin'
1 = vei primi o PAGINA=html
2 = se extrage 'csrfmiddlewaretoken' : 'ETuTwFZFJWFiXjIYD540f27VkaWxJDjWkuoqzilTkZinvIezyCUghtPdHTWzW0iA'
3 = se va adauga la[USERNAME/PASSWORD]care sunt trimise pe POST
'username' : 'andrei'
'password' : '00aaa!!!'
'csrfmiddlewaretoken' : 'ETuTwFZFJWFiXjIYD540f27VkaWxJDjWkuoqzilTkZinvIezyCUghtPdHTWzW0iA'
"""



loginUrl = 'http://127.0.0.1:8000/customlogin/'
cj = CookieJar()

def setupHttpHandler():
    opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
    install_opener(opener)

def httpGet():
    # GET
    response = urlopen(loginUrl).read()

    responseString = response.decode("utf-8") 
    print(responseString)

    return responseString

def httpPost(payload):
    # PREPARE payload for POST
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = Request(url = loginUrl, data = data)

    # POST
    responsePost = urlopen(req).read()
    responseString = responsePost.decode("utf-8") 
    print(responseString)

def printCookies():
    print("the cookies are: ")
    for cookie in cj:
        print(cookie)

def extractMiddlewareToken(responseString, tokenString):
    tokenValueSubstr = ''
    tokenString = 'csrfmiddlewaretoken'
    tokenPos = responseString.find(tokenString)

    valueString = "value=\""
    valuePos = responseString.find(valueString, tokenPos)
    valueLen = len(valueString)

    if tokenPos and valuePos:
        tokenValuePos = valuePos + valueLen
        endOfTokenValue = responseString.find("\"", tokenValuePos)
        tokenValueSubstr = responseString[tokenValuePos : endOfTokenValue]

    return tokenValueSubstr

def composePayload(responseString):
    tokenString = 'csrfmiddlewaretoken'
    tokenValueSubstr = extractMiddlewareToken(responseString, tokenString)
    print("AICI", tokenValueSubstr)

    payload = {'username' : 'andrei',
            'password' : '00aaa!!!' }
    payload[tokenString] = tokenValueSubstr

    return payload


if __name__ == "__main__":
    setupHttpHandler()

    responseString = httpGet()

    printCookies()

    try:
        payload = composePayload(responseString)

        httpPost(payload)

    except HTTPError as error:
        # Need to check its an 404, 503, 500, 403 etc.
        print("Status code ", error.code)
        print("Message ", error.reason)