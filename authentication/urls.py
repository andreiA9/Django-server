from django.urls import path

# LOGIN-VIEW
# from django.contrib.auth.views import LoginView
from .views import CustomLoginView

# HOME PAGE
from django.views.generic.base import TemplateView



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'), # daca nu pui name = 'login' > vei primi EROARE din BROWSER
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
]