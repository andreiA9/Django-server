from django.urls import path
from .views import article_list, article_list_api, article_detail, article_detail_api

urlpatterns = [
	path('article/', article_list),
	path('api/v1/article/', article_list_api),
	path('detail/<int:primaryKey>/', article_detail),
	path('api/v1/detail/<int:primaryKey>/', article_detail_api),
]