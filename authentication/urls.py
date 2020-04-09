from django.urls import path, include

# LOGIN-VIEW
# from django.contrib.auth.views import LoginView
# from .views import CustomLoginView
from . import views


# HOME PAGE
from django.views.generic.base import TemplateView



urlpatterns = [
    # REGISTRATION
    path('register/', views.register, name = 'register'),     # ----------------------------------------------------------------------  |
                                                                                                                                    #   |
                                                                                                                                    #   | REDIRECT  facut prin  
    path('index/', views.index, name = 'index'),            # <-------------------------------------------------------------------------| views.register -> return redirect('index')
                        # name = 'index' este pentru def register(request): -> return redirect('index')

    # LOGIN > redirects to home.html
    path('login/', views.MyLoginView.as_view(), name = 'login'), # daca nu pui name = 'login' > vei primi EROARE din BROWSER        # --|
                        # name = 'login' este pentru <form method="POST" action="{% url 'login' %}">                                #   | REDIRECT facut prin
    # ASTA o faci ca sa nu mai ai                                                                                                   #   | in Settings.py
    # return render(request, 'home.html')                                                                                           #   | LOGIN_REDIRECT_URL = '/'
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # <---------------------------------------------------------|

    path('customlogin/', views.CustomLoginView.as_view(), name = 'customlogin'),

    # ASTA nu se stie ce este cu el
    # django.contrib.auth.urls = URLS included by default by Django\USER MANAGMENET SYSTEM
    path('accounts/', include('django.contrib.auth.urls')),
]