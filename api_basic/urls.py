from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
	path('article/', article_list),
	path('detail/<int:primaryKey>/', article_detail),
]