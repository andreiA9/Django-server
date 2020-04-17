from django.urls import path

from .views import company_list
from .views import company_detail_list


urlpatterns = [
	path('company/', company_list),
    path('company/<int:pk>/', company_detail_list),
]