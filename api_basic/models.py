from django.db import models

""" Models
-un MODEL este o CLASA.a Pyhon care mosteneste django.db.models.Model
-fiecare MODEL.atribut este un CAMP de BAZA=DATE
-MODEL contains METHODS that will allow access to de DATABASE

"""

# Create your models here.
class Article(models.Model):   # INHERITANCE
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str(self):
	    return self.title

""" CLASS = models.Model
CLASA de mai sus creeaza un TABEL in BAZA=DATE
 < CAMP="id" va fi creat automat de REST FRAMEWORK

CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "title" varchar(30) NOT NULL,
    "author" varchar(30) NOT NULL,
    "email" varchar(30) NOT NULL
);
"""