import urllib.request
import urllib.response
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import HTTPBasicAuthHandler
from urllib.request import HTTPError


userName = "andrei"
passWord  = "00aaa!!!"
loginUrl = 'http://127.0.0.1:8000/genericapi/v1/detail/0/'

# create a password manager
passwordManager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passwordManager.add_password(None, loginUrl, userName, passWord)

# create an authorization handler
auth_handler = HTTPBasicAuthHandler(passwordManager)
opener = urllib.request.build_opener(auth_handler)

# OPEN the URL = use the opener to fetch a URL
# opener.open(loginUrl)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

try:
    # VARIANTA1
    request = urllib.request.Request('http://127.0.0.1:8000/genericapi/v1/detail/0/', headers={'Content-Type': 'application/json'})
    # request = urllib.request.Request('http://127.0.0.1:8000/genericapi/v1/detail/0/')
    result = opener.open(request)
    messages = result.read()
    print (messages)

except HTTPError as error:
    print(error.code)
    print(error.reason)