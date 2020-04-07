from django.shortcuts import render

# LOGIN-VIEW
from django.contrib.auth.views import LoginView

# Create your views here.
class CustomLoginView(LoginView):
	member = "mama"

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

# from django.contrib.auth.forms import AuthenticationForm

# class LoginForm(AuthenticationForm):
# 	member = "mama"


# # from . import forms


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