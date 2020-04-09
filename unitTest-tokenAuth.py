import urllib.request
import urllib.response
from urllib.request import Request
from urllib.request import HTTPError


loginUrl = 'http://127.0.0.1:8000/genericapi/v1/detail/0/'

""" !!!! INSTRUCTIUNI
in HEADER ele de PACKET > va trebui sa incluzi urmatorul header
'Authorization' : 'Token ff74d9307bfd1179c1df13443dbbd38fbe525d5d'
"""

if __name__ == "__main__":
    # fara headers ai
    # Status code  401
    # Message  Unauthorized

    # TOKEN-AUTHENTICATION
    # se va include TOKEN ul in HEADER
    req = urllib.request.Request(url = loginUrl, headers={'Authorization': 'Token ff74d9307bfd1179c1df13443dbbd38fbe525d5d'})

    try:
        response = urllib.request.urlopen(req).read()
        print(response)
    except HTTPError as error:
        # Need to check its an 404, 503, 500, 403 etc.
        print("Status code ", error.code)
        print("Message ", error.reason)