from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# @csrf_exempt
from django.views.decorators.csrf import csrf_exempt

# LOGIN-VIEW
from django.contrib.auth.views import LoginView

# REGISTRATION
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login



class CustomLoginView(LoginView):
	member = "mama"

    # if request.method == "POST":
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']

    #     user = authenticate(username=username, password=password)
    #     login(request, user)
        
    #     return redirect('home')




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
            # dai Inspect pe PAGINA=register.html
            # <input type="password" name="password1" autocomplete="new-password" required="" id="id_password1">

            user = authenticate(username=username, password=password)
            login(request, user)
            # return HttpResponse
            return redirect('home') # cauta name='home'
        
        return HttpResponse(status = 403)
    
    elif request.method == "GET":
        form = UserCreationForm()
        args = {'form' : form}   #---------------|  AICI il paseaza ca 
        # return HttpResponse                   \ / PARAMENTRU in register.html
        return render(request, 'registration/register.html', args)

	# Django Login view
	# def login(self, request):
    #     username = request.data['username']
    #     password = request.data['password']
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         serializer = self.serializer_class(user)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     raise AuthenticationFailed



# from . import forms


# class UrdiLoginView(LoginView):
# 	authentication_form = forms.LoginForm

# 	def post(self, request):
# 		webauthentication_form = self.authentication_form(
# 			request=request,
# 			username = request.POST.get('username', None),
# 			password = request.POST.get('password', None),
# 			password2 = request.POST.get('password2', None),
# 			webauthentication_object = json.dumps(
# 				user.get_challenge_from_urdi_user().get('publicKey', '')),
# 			encoding = form.encoding
# 		)
# 		return render(request, 'registation/login.html', {'form': webauthentication_form})