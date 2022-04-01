from django.shortcuts import redirect, render
from django.test import client
from flask import request
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from decouple import config
from .serializers import TodoSerializer 
from rest_framework import viewsets      
from .models import Todo  
import json

DEBUG= config('DEBUG') 
# we write variable name we stored in .env inside quotes

# Create your views here.
def start_page(request):
    user = request.user
    if user.is_authenticated:
        return redirect(home_page)
    else:
        return render(request, "event/index.html")

def home_page(request):
    user = request.user

    auth0_user = user.social_auth.get(provider='auth0')

    user_data={
        'user_id':auth0_user.uid,
        'name':user.first_name,
        'picture':auth0_user.extra_data['picture']
    }

    context = {
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }
    return render(request, "event/home.html",context)

def profile(request):
    user = request.user

    auth0_user = user.social_auth.get(provider='auth0')

    user_data={
        'user_id':auth0_user.uid,
        'name':user.first_name,
        'picture':auth0_user.extra_data['picture']
    }

    context = {
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }

    return render(request,"event/profile.html",context)

def logout(request):
    django_logout(request)

    domain=config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to='http://127.0.0.1:8000'

    return HttpResponseRedirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all()     