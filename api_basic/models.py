from django.db import models

# Create your models here.
class Article (models.Model):   # INHERITANCE
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str(self):
	    return self.title