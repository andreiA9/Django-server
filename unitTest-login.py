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


class HttpPacketHandler:
    def __init__(self, url):
        self.cookies = CookieJar()
        self.url = url

    def setup(self):
        opener = build_opener(HTTPCookieProcessor(self.cookies), HTTPHandler())
        install_opener(opener)

    def get(self):
        # GET
        response = urlopen(self.url).read()

        responseString = response.decode("utf-8")
        print("RESPONSE \n")
        print(responseString)

        return responseString

    def post(self, payload):
        # PREPARE payload for POST
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = Request(url = self.url, data = data)

        # POST
        responsePost = urlopen(req).read()
        responseString = responsePost.decode("utf-8")
        
        print("RESPONSE \n")
        print(responseString)
    
    def setUrl(self, url):
        self.url = url

    def printCookies(self):
        print("\nthe cookies are: ")
        for cookie in self.cookies:
            print(cookie.name, cookie.value, cookie.domain)
        print("\n")

    def extractMiddlewareToken(self, responseString, tokenString):
        tokenValueSubstr = ''
        tokenPos = responseString.find(tokenString)

        valueString = "value=\""
        valuePos = responseString.find(valueString, tokenPos)
        valueLen = len(valueString)

        if tokenPos and valuePos:
            tokenValuePos = valuePos + valueLen
            endOfTokenValue = responseString.find("\"", tokenValuePos)
            tokenValueSubstr = responseString[tokenValuePos : endOfTokenValue]

        return tokenValueSubstr

    def composePayload(self, responseString):
        tokenString = 'csrfmiddlewaretoken'
        tokenValueSubstr = self.extractMiddlewareToken(responseString, tokenString)
        print("MIDDLEWARE-TOKEN")
        print("csrfmiddlewaretoken", tokenValueSubstr)
        print("\n")

        payload = {'username' : 'andrei',
                'password' : '00aaa!!!' }
        payload[tokenString] = tokenValueSubstr

        return payload


if __name__ == "__main__":
    httpHandler = HttpPacketHandler(loginUrl)

    httpHandler.setup()

    responseString = httpHandler.get()

    httpHandler.printCookies()

    try:
        payload = httpHandler.composePayload(responseString)

        httpHandler.post(payload)

    except HTTPError as error:
        # Need to check its an 404, 503, 500, 403 etc.
        print("Status code ", error.code)
        print("Message ", error.reason)