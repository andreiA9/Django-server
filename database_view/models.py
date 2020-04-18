from django.db import models
"""
CE ESTE AICI vei vedea in FISIERUL = Code - model - oneToMany - foreignKey.txt
    -> care are ca COPRESPONDENT = SQL - Inner join - oneToMany.txt
CE ESTE AICI vei vedea in FISIERUL = Code - model - manyToMany - foreignKey.txt
    -> care are ca COPRESPONDENT = SQL - Inner join - manyToMany.txt

IAR tot FLOW ul in SQL il vei vedea in FISIERUL = SQL - example database queries.txt
"""


# GLOBAL VARIABLES
g_COMPANY_INTEL = 0
g_COMPANY_APPLE = 1
g_COMPANY_MICROSOFT = 2



class Company(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


""" RELATIONSHIP = 1-TO-MANY
a PROGRAMMER can be related to a single-COMPANY
"""


class Programmer(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
                                # on_delete = THIS MEANS that when DELETING the COMPANY >
                                # it will need to CASCADE and PROGRAMMERS also
    
    def __str__(self):
        return self.name


""" RELATIONSHIP = MANY-TO-MANY
a LANGUAGE can be known by multiple-PROGRAMMERS
1PROGRAMMER can know many LANGUAGES
"""

class Language(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    programmers = models.ManyToManyField(Programmer)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name




# OBJECT MANAGER for INTEL
class IntelManager(models.Manager):
    def get_queryset(self):
        companies = Company.objects.all()
        return companies[g_COMPANY_INTEL].programmer_set.all()


# OBJECT MANAGER for APPLE
class AppleManager(models.Manager):
    def get_queryset(self):
        companies = Company.objects.all()
        return companies[g_COMPANY_APPLE].programmer_set.all()


# OBJECT MANAGER for MICROSOFT
class MicrosoftManager(models.Manager):
    def get_queryset(self):
        companies = Company.objects.all()
        return companies[g_COMPANY_MICROSOFT].programmer_set.all()