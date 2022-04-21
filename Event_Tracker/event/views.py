from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.test import client
from django.urls import reverse
from flask import request
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from decouple import config
from .serializers import TodoSerializer 
from rest_framework import viewsets      
from .models import Event, Event_Socials, Event_Users, Todo  
from .Event_forms import NameForm,SocialForm
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
    print(user_data)

    context = {
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }

    form_class = SocialForm
    # form_class1 = SocialForm
    # if this is a POST request we need to process the form data
    form = form_class(request.POST or None)
    # form1 = form_class1(request.POST or None)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # form1 = SocialForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    #else:
       # form = NameForm()


    return render(request, "event/home.html",{'form': form})


def home_save_form(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("home-page"))
    else:
        eventname=request.POST.get("event_name")
        eventloc=request.POST.get("event_location")
        eventorg=request.POST.get("event_org")
        eventstart=request.POST.get("event_start_date")
        eventend=request.POST.get("event_end_date")
        twitter=request.POST.get("twitter")
        instagram=request.POST.get("instagram")
        facebook=request.POST.get("facebook")
        event_user_bio=request.POST.get("user_bio")
        user_fname=request.POST.get("fname")
        user_lname=request.POST.get("lname")
        event_username=request.POST.get("username")
        event_phone=request.POST.get("phone")
        event_email=request.POST.get("email")
        try:
            event_user=Event_Users(fname=user_fname, lname=user_lname,username=event_username,phone=event_phone,email=event_email)
            event_user.save()
            event_create=Event(event_name=eventname, event_loc=eventloc, event_org=eventorg,event_start=eventstart,event_end=eventend)
            event_create.save()
            social_media=Event_Socials(twitter=twitter,facebook=facebook,instagram=instagram,user_bio=event_user_bio)
            social_media.save()
            messages.success(request, "Data Save Successfully")
            return HttpResponseRedirect(reverse("home-page"))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse("home-page"))


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