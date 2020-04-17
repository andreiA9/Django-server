from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# @csrf_exempt
from django.views.decorators.csrf import csrf_exempt



# from HERE LOGIN

# LOGIN-VIEW
from django.contrib.auth.views import LoginView

# LOGIN
from django.contrib.auth import login

# LOGOUT
from django.contrib.auth import logout

# REGISTRATION
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# LOGIN REQUIRED
from django.contrib.auth.decorators import login_required



class MyLoginView(LoginView):
	member = "mama"


class CustomLoginView(LoginView):

    def get(self, request):
        form = self.get_form()
        args = {'form' : form}
        return render(request, 'registration/customlogin.html', args)

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        file = open("output.txt", 'w')
        file.write("register username: %s \n" % username)
        file.write("register password: %s \n" % password)
        file.close()

        user = authenticate(username=username, password=password)
        if user is not None:
            # login() saves the user’s ID in the session, using Django’s session framework.
            login(request, user)

            # return HttpResponse
            return redirect('home') # cauta name='home'
        else:
            return HttpResponse(status = 403)


# EXPLICATIILE pentru asta le vei gasi un urls.py la path('login/')
@login_required()
def tryLogin(request):
    return HttpResponse("<h1>You need to be logged in to view this page!</h1>")


# nu denumi sub nicio FORMA FUNCTIA ca fiind
# def logout(request):
# < pentru ca faci override la FUNCTIA logout() a lui Django
def logoutUser(request):
    if request.method == 'GET':
        return render(request, 'logout.html')

    elif request.method == 'POST':
        # aici nu trebuie sa dai PARAMETRU=USER ul pe care trebuie sa
        # il delogheze<pentru ca Django stie ca USER este acum actual
        logout(request)

        return HttpResponse("<h1>You have been logged out!</h1>")



def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid(): # only if the user entered valid DATA
            form.save() # save the USER to DB

            # username = request.data['username']
            # password = request.data['password']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] # aici sunt 2PAROLE in REGISTER.FORM

            file = open("output.txt", 'w')
            file.write("register username: ", username)
            file.write("register password: ", password)
            file.close()

            # dai Inspect pe PAGINA=register.html
            # <input type="password" name="password1" autocomplete="new-password" required="" id="id_password1">

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # return HttpResponse
                return redirect('home') # cauta name='home'
        
        return HttpResponse(status = 403)
    
    elif request.method == "GET":
        form = UserCreationForm()
        args = {'form' : form}   #---------------|  AICI il paseaza ca 
        # return HttpResponse                   \ / PARAMENTRU in register.html
        return render(request, 'registration/register.html', args)