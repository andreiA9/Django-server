from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)

    class Meta:
        abstract = True


class Customer(ContactInfo):
    phone = models.CharField(max_length = 15)


class Staff(ContactInfo):
    phone = models.CharField(max_length = 15)