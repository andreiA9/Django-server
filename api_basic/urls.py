from django.urls import path, include
from .views import article_list, article_list_api

# FUNCTION-based API-VIEW
from .views import article_detail, article_detail_api

# CLASS-based API-VIEW
from .views import ArticleListApiView, ArticleDetailApiView

# GENERIC-VIEW
from .views import GenericApiView

# VIEWSETS
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')
# END VIEWSETS


urlpatterns = [
	# 0 = non-API
	path('article/', article_list),
	path('detail/<int:primaryKey>/', article_detail),
	# 1 = FUNCTION-based API-view
	path('api/v1/article/', article_list_api),
	path('api/v1/detail/<int:primaryKey>/', article_detail_api),
	# 2 = CLASS-based API-view
	path('classapi/v1/article/', ArticleListApiView.as_view()),
	path('classapi/v1/detail/<int:id>/', ArticleDetailApiView.as_view()),
	# 3 = GENERIC API-view
	# + AUTHENTICATION{basic/token}
	# http://127.0.0.1:8000/genericapi/v1/detail/0/ < le da pe toate ELEMENTELE
	# http://127.0.0.1:8000/genericapi/v1/detail/1/ < da 1ELEMENT
	path('genericapi/v1/detail/<int:id>/', GenericApiView.as_view()),
	# 4 = VIEWSETS
	# NOT WORKING < vezi in COD												URL ul va deveni 'viewset/' + 'article' < la care ai facut REGISTER
	# router.register('article', ArticleViewSet, basename = 'article') <------------------------|
																							#  \ /
	path('viewset/', include(router.urls)),					# -> DEVINE http://127.0.0.1:8000/viewset/article/
	path('viewset/<int:pk>/', include(router.urls)),		# -> DEVINE http://127.0.0.1:8000/viewset/article/1/
]