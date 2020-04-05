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
