INSTRUCTIONS

1 = RUN SERVER
python manage.py runserver

2 = SITE ul tau
http://127.0.0.1:8000/article/

3 = RUN UNIT TESTS
python .\unitTest.py

TUTORIAL DJANGO
https://www.youtube.com/watch?v=B38aDwUpcFc
MINUT 01:40:46 - basic-AUTHENTICATION
MINUT 01:49:46 - token-AUTHENTICATION
MINUT 1:56:18 - Viewsets & Routers


!!!!
orice SCHIMBARE in settings.py > inseamna ca va trebui sa faci MIGRATE
! python manage.py migrate



AICI ai TABELELE
http://127.0.0.1:8000/admin/

TABLE = Article         < http://127.0.0.1:8000/admin/api_basic/article/
TABLE = Users           < http://127.0.0.1:8000/admin/auth/user/
TABLE = Groups          < http://127.0.0.1:8000/admin/auth/group/


URL uri IMPLEMENTATE.in acest COD:

0 = non-API
http://127.0.0.1:8000/article/

1 = FUNCTION-based API-view
http://127.0.0.1:8000/api/v1/article/
http://127.0.0.1:8000/api/v1/detail/4/

2 = CLASS-based API-view
http://127.0.0.1:8000/classapi/v1/article/
http://127.0.0.1:8000/classapi/v1/detail/2/

3 = GENERIC API-view
http://127.0.0.1:8000/genericapi/v1/detail/1/

4 = AUTHENTICATION PAGE
http://127.0.0.1:8000/genericapi/v1/detail/0/




TUTORIALE
SERIE.lunga
https://www.youtube.com/channel/UCAx4nmhI7S1RcPiaG-Uw0tg
 |
\ /
PART1
https://www.youtube.com/watch?v=2_yCj2TEFW8