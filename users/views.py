from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.forms import LoginForm


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated():
            context = {
                'usuario_logeado': request.user.username
            }
            return render(request, 'views/index.html', context)
        else:
            return redirect('users_login')


class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors' : error_messages,
            'login_form' : form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    #url = request.GET.get('next', 'home')
                    #return redirect(url)
                    return redirect('/static/facturacion/prueba.html')
                else:
                    error_messages.append("El usuario no está activo")

        context = {
            'errors' : error_messages,
            'login_form' : form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('home')


class LogoutAPI(APIView):
    queryset = User.objects.all()

    def get(self, request):
        # Borramos el token
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
