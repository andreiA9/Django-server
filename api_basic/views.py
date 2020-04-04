from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt # needed for @csrf_exempt to work


# if you do not write this when POSTING > you will receive an STATUS=501 < "Internal server error"
@csrf_exempt

# Create your views here.
def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many = True)
		return JsonResponse(serializer.data, safe = False)
	
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(data = data)
		
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
									# STATUS = 201 < 'created'
		
		return JsonResponse(serializer.errors, status=400)
									# STATUS = 400 < 'Bad Request'
