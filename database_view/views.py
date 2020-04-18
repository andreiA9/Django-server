from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response

# MODELS and MANAGERS
from .models import Company
from .models import Programmer
from .models import Language
from .models import IntelManager
from .models import AppleManager
from .models import MicrosoftManager

# SERIALIZERS
from .serializers import CompanySerializer
from .serializers import ProgrammerSerializer

# HTTP RESPONSES
from django.http import JsonResponse

# @csrf_exempt
from django.views.decorators.csrf import csrf_exempt



# GLOBAL VARIABLES
g_COMPANY_INTEL = 0
g_COMPANY_APPLE = 1
g_COMPANY_MICROSOFT = 2




class ItemViewSet(viewsets.ModelViewSet):
    mama = "mama"



class CompaniesListing(TemplateView):
    template_name = 'companies.html'

    def get_context_data(self, **kwargs):
        companies = Company.objects.all()
        context = {'companies': companies}
        return context


class ProgrammersListing(TemplateView):
    template_name = 'programmers.html'

    def get_context_data(self, **kwargs):
        programmers = Programmer.objects.all()
        context = {'programmers': programmers}
        return context


class LanguagesListing(TemplateView):
    template_name = 'languages.html'

    def get_context_data(self, **kwargs):
        languages = Company.objects.all()
        context = {'languages': languages}
        return context



@csrf_exempt
def company_detail_list(request, pk):
    company = Company.objects.get(pk = pk)
    serializer = CompanySerializer(company)

    return JsonResponse(serializer.data)


@csrf_exempt
def listCompanyProgrammers(request, primaryKey):
    if primaryKey == g_COMPANY_INTEL:
        # get OBJET MANAGER for INTEL
        intelProgrammers = IntelManager()
        serializer = ProgrammerSerializer(intelProgrammers, many = True)
        
        # False = In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(serializer.data, safe = False)
    elif primaryKey == g_COMPANY_APPLE:
        # get OBJET MANAGER for APPLE
        appleProgrammers = AppleManager()
        serializer = ProgrammerSerializer(appleProgrammers, many = True)
        
        # False = In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(serializer.data, safe = False)
    elif primaryKey == g_COMPANY_MICROSOFT:
        # get OBJET MANAGER for MICROSOFT
        microsoftProgrammers = MicrosoftManager()
        serializer = ProgrammerSerializer(microsoftProgrammers, many = True)
        
        # False = In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(serializer.data, safe = False)