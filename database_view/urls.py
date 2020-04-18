from django.urls import path

from .views import CompaniesListing
from .views import ProgrammersListing
from .views import LanguagesListing
from .views import company_detail_list
from .views import listCompanyProgrammers


urlpatterns = [
	path('companies/', CompaniesListing.as_view()),
    path('programmers/', ProgrammersListing.as_view()),
    path('languages/', LanguagesListing.as_view()),
    path('company/<int:pk>/', company_detail_list),
    path('company/<int:primaryKey>/programmers/', listCompanyProgrammers),
]