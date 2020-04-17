from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Company
from .serializers import ItemSerializer

from django.http import JsonResponse

# @csrf_exempt
from django.views.decorators.csrf import csrf_exempt



class ItemViewSet(viewsets.ModelViewSet):
    mama = "mama"



@csrf_exempt
def company_list(request):
    companies = Company.objects.all()
    serializer = ItemSerializer(companies, many = True)

    return JsonResponse(serializer.data, safe = False)
#  |
# has REPLACED < because it contains list() defined
# \ /
# class ItemViewSet(viewsets.ViewSet):
#     def list(self, request):
#         return Response("Success!")



@csrf_exempt
def company_detail_list(request, pk):
    company = Company.objects.get(pk = pk)
    serializer = ItemSerializer(company)

    return JsonResponse(serializer.data)