AUTHENTICATION.methods

0=basic-AUTHENTICATION
	-> used only for TESTING PURPOSES < should not be used in PRODUCTION
THEORY
-(if you used BasicAuthentication in PRODUCTION>you
 must ensure that your API is only available over
 HTTPS)-(you should also ensure that your API-
 clients will always re-request the username and
 password at login, and will never store those
 details to persistent storage =?? DATABASE (nu
 stii sigur daca asta inseamna)

1=session-AUTHENTICATION
-(this uses Django's default session backend for
 authentication)-(session authentication is appropiate
 for AJAX clients that are running in the same
 session-context as your website)

2=token-AUTHENTICATION
THEORY
-(this authetication scheme uses a simple token-based HTTP
 Authentication scheme)-(token-AUTHENTICATION is appropiate
 for client-server setups<such as native-DESKTOP and MOBILE-
 CLIENTS)=>(deci cea de la DRS Django Frontend nu poate sa
 fie[BasicAuthentication/SessionAuthentication]<pentru ca
 este CLIENT=DESKTOP-BROWSER)



!!!!
CODE for[
CLASS-based API-view /
GENERIC API-view]

You can also set the authentication scheme on a per-view or per-viewset
 basis, using the APIView class-based views.

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)



!!!!
CODE for[
FUNCTION-based API-view]

Or, if you're using the @api_view decorator with function based views.

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)



INSTRUCTIONS for
ERROR

0 = LOGIN
http://127.0.0.1:8000/admin/

1 = ACCESS this URL < when being logged in
http://127.0.0.1:8000/genericapi/v1/detail/0/

2 = LOGOUT
http://127.0.0.1:8000/admin/

3 = ACCESS again the URL at STEP=1
http://127.0.0.1:8000/genericapi/v1/detail/0/
ERROR
"detail": "Authentication credentials were not provided."



INSTRUCTIONS
POSTMAN

0 = choose=GET < aici nu e POST!!!!
1 = tab=Authorization
    -> TYPE = Basic Auth -> Username = andrei (admin)
                         -> Password = 00aaa!!!

ERROR
2 = tab=Authorization
    -> TYPE = Inherit from parent -> Username = andrei (admin)
                                  -> Password = 00aaa!!!
"detail": "Authentication credentials were not provided."
