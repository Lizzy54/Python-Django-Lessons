from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

def login(request):
    if request.method == "GET":
        return render(request, 'auth/login.html', {'user': request.user, 'login_error': 0})
    elif request.method == "POST":
        user = authenticate(
            request, 
            username = request.POST['username'], 
            password = request.POST['password'])
        if user is None:
            return render(request, 'auth/login.html', {'user': request.user, 'login_error': 1})
        else:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == "GET":
        return render(request, 'auth/register.html', {'user': request.user, 'email_error': 0, 'username_error': 0})
    elif request.method == "POST":
        if User.objects.filter( email = request.POST['e-mail'] ).exists():
            return render(request, 'auth/register.html', {'user': request.user, 'email_error': 1, 'username_error': 0})
        else:
            if User.objects.filter( username = request.POST['username'] ).exists():
                return render(request, 'auth/register.html', {'user': request.user, 'email_error': 0, 'username_error': 1})
            else:
                new_user = User.objects.create_user(
                    first_name = request.POST['name'],
                    last_name = request.POST['lastname'],
                    email = request.POST['e-mail'],
                    username = request.POST['username'],
                    password = request.POST['password'])
        
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        auth_login(request, user)
        return HttpResponseRedirect('/')