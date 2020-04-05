from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer

from django.views.decorators.csrf import csrf_exempt # needed for @csrf_exempt to work

# API_VIEW
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# @csrf_exempt
# def article_list(request):

# if you do not write this when POSTING > you will receive an STATUS=501 < "Internal server error"
@api_view(['GET', 'POST'])			# < ASTA a fost = @csrf_exempt
def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many = True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		# NOT NEEDED when USING an API VIEW
		# data = JSONParser().parse(request)
		serializer = ArticleSerializer(data = request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
									# STATUS = 201 < 'created'
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
									# STATUS = 400 < 'Bad Request'


# @csrf_exempt(['GET', 'POST'])		# < ASTA a fost = @csrf_exempt
# def article_list(request):
# 	if request.method == 'GET':
# 		articles = Article.objects.all()
# 		serializer = ArticleSerializer(articles, many = True)
# 		return JsonResponse(serializer.data, safe = False)
	
# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = ArticleSerializer(data = data)
		
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status = 201)
# 									# STATUS = 201 < 'created'
		
# 		return JsonResponse(serializer.errors, status = 400)
# 									# STATUS = 400 < 'Bad Request'



# FUNCTION-based API-view
@csrf_exempt
def article_detail(request, primaryKey):
	try:
		article = Article.objects.get(pk = primaryKey)
	except Article.DoesNotExist:
		return HttpResponse(status = 404)
	
	if request.method == 'GET':
		serializer = ArticleSerializer(article)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(article, data = data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
									# STATUS = 201 < 'created'
		
		return JsonResponse(serializer.errors, status = 400)
									# STATUS = 400 < 'Bad Request'

	elif request.method == 'DELETE':
		article.delete()
		return HttpResponse(status = 204)
									# STATUS = 204 < 'No Content'

# csrf_exempt =
# Note that because we want to be able to POST to this view from clients that won't have a CSRF token > we
# need to mark this view as csrf_exempt. This isn't something that you'd normally want to do., and the REST
# framework views actually use more sensible behaviour than this, but it'll do for our purposes right now