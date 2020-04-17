"""
FISIERUL.acesta este identic cu unitTest-login ! dar are adaugata partea de logout() >
 incat a fost adaugat o CLASA=Client
"""

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

""" EXPLICATII AUTENTIFICARE
0=la LOGIN imediat ce apesi BUTON=SUBMIT>se vor trimite
 CREDENTIALE=DATELE.de AUTENTFICARE[username/password]
1=la LOGIN in FORM care contine SUBMIT este specificata
 METODA="POST"<prin care sunt trimise DATELE pentru
 AUTENTIFICARE)-(DATELE sunt trimise exact ca mai jos)
"""


""" !!!! INSTRUCTIUNI

LOGIN
 < vezi in POST - login.png
pentru login se va proceda in felul urmator:
0 = se face un GET la URL='customlogin'
1 = vei primi o PAGINA=html
2 = se extrage 'csrfmiddlewaretoken' : 'ETuTwFZFJWFiXjIYD540f27VkaWxJDjWkuoqzilTkZinvIezyCUghtPdHTWzW0iA'
3 = vei primi un COOKIE = adica 
'Set-Cookie' : 'csrftoken=wCoPEZ3JbAjXnhpr8cTvuPV7Xf4RlA6Yod4MFDDc3bj8eUmvKwhZFn995sFiZXE2'
    3.1 dupa ce ai extras COOKIE ul de mai sus > va trebui sa il trimiti inapoi de asemenea scris exact asa in ENTRY = 'Set-Cookie'
    {'Set-Cookie': 'csrftoken=ientbDbQa1wu5UhWnsz8HSHp2VdAzzyLIfNLlfJuGqvSAsaUqnWlECVw4Xe2Gp0s'}
4 = se va adauga la[USERNAME/PASSWORD]care sunt trimise pe POST la URL=LOGIN
    4.1 se vor trimite in POST DATELE.uumatoare
        'username' : 'andrei'
        'password' : '00aaa!!!'
        'csrfmiddlewaretoken' : 'ETuTwFZFJWFiXjIYD540f27VkaWxJDjWkuoqzilTkZinvIezyCUghtPdHTWzW0iA'


LOGOUT
 < vezi in POST - logout.png
pentru logout se va proceda exact ca mai sus la LOGIN:
0 = se face un GET la URL='customlogin'
1 = vei primi o PAGINA=html
2 = se extrage 'csrfmiddlewaretoken' : 'ETuTwFZFJWFiXjIYD540f27VkaWxJDjWkuoqzilTkZinvIezyCUghtPdHTWzW0iA'
3 = vei primi 2COOKIE uri = adica 
'Set-Cookie' : 'csrftoken=wCoPEZ3JbAjXnhpr8cTvuPV7Xf4RlA6Yod4MFDDc3bj8eUmvKwhZFn995sFiZXE2'
'Set-Cookie' : 'sessionid=85h7j9ebb9eran1fpii35thuanhegy15'
    0.1 dupa ce ai extras COOKIE urile de mai sus > va trebui sa le trimiti pe amandoua inapoi de asemenea scris exact asa in ENTRY = 'Set-Cookie'
    {'Set-Cookie': 'csrftoken=ientbDbQa1wu5UhWnsz8HSHp2VdAzzyLIfNLlfJuGqvSAsaUqnWlECVw4Xe2Gp0s'}
    {'Set-Cookie': 'sessionid=85h7j9ebb9eran1fpii35thuanhegy15'}
4 = se va adauga la[USERNAME/PASSWORD]care sunt trimise pe POST la URL=LOGOUT
    1.1 se vor trimite in POST DATELE.uumatoare
        'csrfmiddlewaretoken' : 'ETuTwFZFJWFiXjIYD540f27VkaWxJDjWkuoqzilTkZinvIezyCUghtPdHTWzW0iA'
"""


loginUrl = 'http://127.0.0.1:8000/customlogin/'
logoutUrl = 'http://127.0.0.1:8000/logout/'


class HttpPacketHandler:
    def __init__(self):
        self.cookies = CookieJar()
        self.middlewareToken = {}

    def setup(self):
        opener = build_opener(HTTPCookieProcessor(self.cookies), HTTPHandler())
        install_opener(opener)

    def get(self, url):
        response = urlopen(url).read()

        responseString = response.decode("utf-8")
        print("\nGET RESPONSE \n")
        print(responseString)

        return responseString
    
    def createCustomCookie(self):
        csrfTokenCookie = {}
        for cookie in self.cookies:
            cookieName = cookie.name + '=' + cookie.value
            # NU SCHIMBA 'Set-Cookie' < pentru ca nu mai merge
            csrfTokenCookie = {'Set-Cookie' : cookieName}
            # aici cauta in BROWSER < apasand F12 >
            # in HEADER e vei gasi COOKIE urile presetate de TINE
            # 'Cookie' : csrftoken=AIIW2VovyevVGAZhjSaF1tbIVPfJnCgnSlQn9r3aLDq76bcwiVtGgdUAIojrbbX4
            # acesta este un COOKIE presetata doar de DJANGO WEB APPLICATIONS
            print(csrfTokenCookie)
        
        return csrfTokenCookie

    def post(self, url, payload):
        # PREPARE payload for POST
        data = urllib.parse.urlencode(payload).encode("utf-8")

        postCookie = self.createCustomCookie()

        # aici trebuie sa fie headers = {} < DICT
        req = Request(url = url, data = data, headers = postCookie)

        # POST
        responsePost = urlopen(req).read()
        
        # AICI vei primi toata PAGINA inapoi
        print("\nPOST RESPONSE \n")
        responseString = responsePost.decode("utf-8")
        print(responseString)
    
    def printCookies(self):
        print("\nthe cookies are: ")
        for cookie in self.cookies:
            print(cookie.name, cookie.value, cookie.domain)
        print("\n")

    def extractMiddlewareToken(self, responseString, tokenString):
        middlewareToken = ''
        tokenPos = responseString.find(tokenString)

        valueString = "value=\""
        valuePos = responseString.find(valueString, tokenPos)
        valueLen = len(valueString)

        if tokenPos and valuePos:
            tokenValuePos = valuePos + valueLen
            endOfTokenValue = responseString.find("\"", tokenValuePos)
            middlewareToken = responseString[tokenValuePos : endOfTokenValue]

        return middlewareToken
    
    def fillCredentials(self):
        payload = {'username' : 'andrei',
                  'password' : '00aaa!!!' }
        
        return payload

    def composePayload(self, responseString, isLogin = False):
        tokenString = 'csrfmiddlewaretoken'
        middlewareToken = self.extractMiddlewareToken(responseString, tokenString)
        print("MIDDLEWARE-TOKEN")
        print("csrfmiddlewaretoken", middlewareToken)
        print("\n")

        payload = self.fillCredentials() if isLogin == True else {}
        payload[tokenString] = middlewareToken

        return payload

class HttpClient:
    def __init__(self):
        self.httpHandler = HttpPacketHandler()

        self.httpHandler.setup()

    def login(self):
        try:
            # AICI vei PRIMI inapoi toata PAGINA=LOGIN = customLogin.html
            print('\nPAGINA = CUSTOM LOGIN \n')
            responseString = self.httpHandler.get(loginUrl)

            self.httpHandler.printCookies()

            # se extrage TOKEN ul de la LOGIN < este UNIC per USER ul tau
            # acest TOKEN va fi generat ca fiind NOU)<=(din CAUZA ca te 
            # stie ca te ai autentificat pe SITE ca CLIENT cu un IP)
            payload = self.httpHandler.composePayload(responseString, isLogin = True)

            # AICI vei PRIMI inapoi toata PAGINA=HOME = http://127.0.0.1:8000/
            print('\nPAGINA = HOME \n')
            self.httpHandler.post(loginUrl, payload)

        except HTTPError as error:
            print("Status code ", error.code)
            print("Message ", error.reason)
    
    def logout(self):
        try:
            responseString = self.httpHandler.get(loginUrl)

            self.httpHandler.printCookies()

            # se extrage TOKEN ul de la LOGIN < este UNIC per USER ul tau
            # acest TOKEN va fi generat ca fiind NOU)<=(din CAUZA ca te 
            # stie ca te ai autentificat pe SITE ca CLIENT cu un IP)
            payload = self.httpHandler.composePayload(responseString, isLogin = True)

            self.httpHandler.post(logoutUrl, payload)

        except HTTPError as error:
            print("Status code ", error.code)
            print("Message ", error.reason)


if __name__ == "__main__":
    client = HttpClient()
    client.login()

    client.logout()