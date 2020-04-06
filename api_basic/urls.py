from django.urls import path
from .views import article_list, article_list_api
# FUNCTION-based API-view
from .views import article_detail, article_detail_api
# CLASS-based API-view
from .views import ArticleListApiView, ArticleDetailApiView

urlpatterns = [
	path('article/', article_list),
	path('api/v1/article/', article_list_api),
	path('classapi/v1/article/', ArticleListApiView.as_view()),
	path('detail/<int:primaryKey>/', article_detail),
	path('api/v1/detail/<int:primaryKey>/', article_detail_api),
	path('classapi/v1/detail/<int:id>/', ArticleDetailApiView.as_view())
]