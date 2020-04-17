import osimpry sys
import logging
import argparse
import pprint
import time
import json
import re

# HTTP
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



g_loginUrl = '/en/login/'
g_logoutUrl = '/logout/'
g_warrantsUrl = 'api/v1/warrants/'
g_warrantsPage = '/?page'
g_lockUrl = 'ap1/v1/280/lock/'
g_unlockUrl = 'ap1/v1/280/unlock/'
g_activateUrl = 'ap1/v1/280/activate/'
g_archiveUrl = 'ap1/v1/280/archive/'
g_queryResultsUrl = 'api/v1/warrants/280/results/123/'


# !!!!
# AI RAMAS

class RestController:
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
        self.httpHandler = RestController()

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