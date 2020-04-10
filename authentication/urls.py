from django.urls import path, include

# LOGIN-VIEW
from .views import CustomLoginView
from .views import MyLoginView
from . import views


# HOME PAGE
from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required


urlpatterns = [
    # REGISTRATION
    # pentru REGISTER trebuie POST
    path('register/', views.register, name = 'register'),     # --------------------------------------------------------|
                                                                                                                    #   |
                                                                                                                    #   | REDIRECT  facut prin  
    path('index/', views.index, name = 'index'),            # <---------------------------------------------------------| views.register -> return redirect('index')
                        # name = 'index' este pentru def register(request): -> return redirect('index')

    
    # LOGIN implemented with LoginView
    # LOGIN > redirects to home.html
    # LOGIN ul din aceasta PAGINA este identic cu LOGIN ul din PAGINA='admin/'
    path('login/', MyLoginView.as_view(), name = 'login'), # daca nu pui name = 'login' > vei primi EROARE din BROWSER    # --|
                        # name = 'login' este pentru <form method="POST" action="{% url 'login' %}">                      #   | REDIRECT facut prin
    # ASTA o faci ca sa nu mai ai                                                                                         #   | in Settings.py
    # return render(request, 'home.html')                                                                                 #   | LOGIN_REDIRECT_URL = '/'
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # <-----------------------------------------------|

    path('customlogin/', CustomLoginView.as_view(), name = 'customlogin'),

    path('loginrequired/', views.tryLogin, name="trylog"),
    # INSTRUCTIUNI
    # daca vei incerca sa te conectezi la PAGINA.aceasta='loginrequired/' > nu te va lasa)=>
    # (intrucat te va redirectiona la PAGINA='login/')-(dupa ce ai fost logat 'login/' te va
    # redirectiona la 'home/')=>(de aceea va trebui sa deschizi inca o data 
    # PAGINA='loginrequired/'>pentru a putea sa vezi CONTENT ul ei=adica ce este in functia
    # def tryLogin(request))

    # LOGIN implemented with simple function ! no Logout view
    # pentru LOGOUT trebuie POST
    path('logout/', views.logoutUser, name="logout"),
]