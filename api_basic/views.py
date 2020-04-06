from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer

from django.views.decorators.csrf import csrf_exempt # needed for @csrf_exempt to work

# FUNCTION-based API-VIEW
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# CLASS-based API-VIEW
from rest_framework.views import APIView

# GENERIC-VIEW
from rest_framework import generics
from rest_framework import mixins

# SESSION AUTHENTICATION
from rest_framework.authentication import SessionAuthentication	# AUTHENTICATION
from rest_framework.authentication import BasicAuthentication	# AUTHENTICATION
from rest_framework.permissions import IsAuthenticated			# PERMISSIONS



# if you do not write this when POSTING > you will receive an STATUS=501 < "Internal server error"
@csrf_exempt
def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many = True)
		return JsonResponse(serializer.data, safe = False)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(data = data)
		
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
									# STATUS = 201 < 'created'
		
		return JsonResponse(serializer.errors, status = 400)
									# STATUS = 400 < 'Bad Request'


# FUNCTION-based API-view
@api_view(['GET', 'POST'])			# < ASTA a fost = @csrf_exempt
def article_list_api(request):
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


# CLASS-based API-view
# ASTA este IDENTICA cu FUNCTION-based API-view
class ArticleListApiView(APIView):
	# !!!!
	# este identica cu FUNCTIA = article_list_api(request)
	def get(self, request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many = True)
		return Response(serializer.data)
	
	def post(self, request):
		serializer = ArticleSerializer(data = request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
									# STATUS = 201 < 'created'
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#  |
# \ /
# THEORY
# REST framework provides an APIView class, which subclasses Django's View class.
# APIView classes are different from regular View classes in the following ways:
# 0=Requests passed to the handler methods will be REST framework's Request instances,
#  not Django's HttpRequest instances.
# 1=Handler methods may return REST framework's Response, instead of Django's
#  HttpResponse. The view will manage content negotiation and setting the correct
#  renderer on the response.
# 2=Any APIException exceptions will be caught and mediated into appropriate
#  responses.
# 3=Incoming requests will be authenticated and appropriate permission and/or
#  throttle checks will be run before dispatching the request to the handler method.
# Using the APIView class is pretty much the same as using a regular View class, as
#  usual, the incoming request is dispatched to an appropriate handler method such as
#  .get() or .post().




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


# FUNCTION-based API-view
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api(request, primaryKey):
	try:
		article = Article.objects.get(pk = primaryKey)
	except Article.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = ArticleSerializer(article)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ArticleSerializer(article, data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
									# STATUS = 201 < 'created'
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
									# STATUS = 400 < 'Bad Request'

	elif request.method == 'DELETE':
		article.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
									# STATUS = 204 < 'No Content'


# CLASS-based API-view
# ASTA este IDENTICA cu FUNCTION-based API-view
# MINUTUL 16
class ArticleDetailApiView(APIView):
	def get_object(self, id):
		try:
			return Article.objects.get(id = id)
		except Article.DoesNotExist:
			return Response(status = status.HTTP_404_NOT_FOUND)
	
	def get(self, request, id):
		article = self.get_object(id = id)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)
	
	def put(self, request, id):
		article = self.get_object(id = id)
		serializer = ArticleSerializer(article, data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
									# STATUS = 201 < 'created'
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
									# STATUS = 400 < 'Bad Request'
	
	def delete(self, request, id):
		article = self.get_object(id = id)	
		article.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
									# STATUS = 204 < 'No Content'


# mixins.ListModelMixin 	-> pentru self.list() din get()			< iti apare GET in API-VIEW
# mixins.RetrieveModelMixin -> pentru self.retrieve() din get()
# mixins.CreateModelMixin	-> pentru self.create() din post()		< iti apare POST in API-VIEW
# mixins.UpdateModelMixin 	-> pentru self.update() din put()		< iti apare POST in API-VIEW
# mixins.DestroyModelMixin 	-> pentru self.retrieve() din delete()	< 
class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
					mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
					mixins.DestroyModelMixin):
	serializer_class = ArticleSerializer
	
	# asta este pentru [get() / post()]
	queryset = Article.objects.all()	# aici in TUTORIAL era "query_set" < pentru ca au mai schimbat ceva
	#asta este pentru put() < pentru ca avea nevoie de primaryKey
	lookup_field = 'id'

	# AUTHENTICATION < aici sunt amandoua [SessionAuthentication, BasicAuthentication]
	# this means that it will be searched for a SessionAuthentication <
	# if this is not found > then it will be used the BasicAuthentication
	authentication_classes = [SessionAuthentication, BasicAuthentication] 	# = LIST
	permission_classes = [IsAuthenticated]									# = LIST

	def get(self, request, id = None):
		# localhost:8000/genericapi/v1/detail/1/ < this can be any number
		if id:
			return self.retrieve(request)
		
		# in CAZUL.acesta ti le va arata pe toate
		# localhost:8000/genericapi/v1/detail/0/
		elif id == 0:
			return self.list(request)
	
	def post(self, request):
		return self.create(request)
	
	def put(self, request, id = None):
		return self.update(request, id)
	
	def detele(self, request, id = None):
		return self.destroy(request, id)