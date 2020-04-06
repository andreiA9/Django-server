http://127.0.0.1:8000/article/
BRANCH = 1-articles-page


CORRECT POST
{
    "title": "Title4",
    "author": "Ana",
    "email": "ana@yahoo.com"
}

INCORRECT POST
[{
    "title": "Title2",
    "author": "Costel",
    "email": "costel@yahoo.com"
}]
 |
\ /
STATUS = Bad Request


OPERATII.pe BAZA=DATE
1 = POST (de sus) = PUT pe mai multe ELEMENTE
    -> article/
    
2 = PUT (de jos) = PUT pe un ELEMENT
 	-> detail/int/  < PUT va inlocui ELEMENTUL.curent


INSTRUCTIONS
POSTMAN

at GET
0 = choose=GET
1 = click=Send
    -> check=Status
    -> find RESULTS at tab=Params

at POST
0 = choose=POST
1 = tab=Body
    -> check=raw
    -> choose=JSON
2 = click=Send
    -> check=Status
    -> find RESULTS at tab=Params