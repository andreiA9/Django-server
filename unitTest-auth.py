from urllib.request import urlopen
from urllib.request import build_opener
from urllib.request import install_opener
from urllib.request import HTTPBasicAuthHandler
from urllib.request import HTTPError

loginUrl = 'http://127.0.0.1:8000/genericapi/v1/detail/0/'

auth_handler = HTTPBasicAuthHandler()
auth_handler.add_password(realm = loginUrl,
                         uri = '',
                         user = 'andrei',
                         passwd = '00aaa!!!')

opener = build_opener(auth_handler)
install_opener(opener)
try:
    responseString = urlopen(loginUrl).read()
    print(responseString)
except HTTPError as error:
    print(error.code)
    print(error.reason)



# from requests.auth import HTTPBasicAuth
# # requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
# responseString = requests.get(loginUrl, auth=HTTPBasicAuth('andrei', '00aaa!!!'))
# print(responseString)


# import urllib.request
# import urllib.response

# userName = "andrei"
# passWord  = "00aaa!!!"
# loginUrl = 'http://127.0.0.1:8000/genericapi/v1/detail/0/'

# # create an authorization handler
# passwordManager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# passwordManager.add_password(None, loginUrl, userName, passWord)

# auth_handler = urllib.request.HTTPBasicAuthHandler(passwordManager)
# opener = urllib.request.build_opener(auth_handler)

# urllib.request.install_opener(opener)
# # try:
# #     responseString = urlopen(loginUrl).read()
# #     print(responseString)
# # except HTTPError as error:
# #     print(error.code)
# #     print(error.reason)

# DATA = b'{"data": { "foo": "bar", "timestamp": 1466593290 }}'
# try:
#     req = urllib.request.Request('http://127.0.0.1:8000/genericapi/v1/detail/0/', data=DATA, headers={'Content-Type': 'application/json'})    
#     result = opener.open(req)
#     messages = result.read()
#     print (messages)
# except IOError as e:
#     print (e)