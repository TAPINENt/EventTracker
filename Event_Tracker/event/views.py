from pickle import FALSE
from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import context
from django.test import client
from django.urls import reverse
from flask import request
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from decouple import config
from .serializers import TodoSerializer 
from rest_framework import viewsets      
from .models import Event, Event_Socials, Event_Users, Event_Host, Todo  
from .Event_forms import NameForm,SocialForm
from django.core.files.storage import FileSystemStorage
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


    return render(request, "event/home.html",context,{'form': form})


def home_save_form(request):
    context = {}
    if request.method!="POST":
        return HttpResponseRedirect(reverse("home-page"))
    else:
        event_name = request.POST.get("event_name")
        event_location = request.POST.get("event_location")
        event_org = request.POST.get("event_org")
        event_img = request.FILES['event_img'] if 'event_img' in request.FILES else False
        if event_img != False:
            fs = FileSystemStorage()
            media_name = fs.save(event_img.name, event_img)
            context['media_url'] = fs.url(media_name)
            print(event_img.size)
        event_start_date = request.POST.get("event_start_date")
        event_end_date = request.POST.get("event_end_date")
        twitter = request.POST.get("twitter")
        instagram = request.POST.get("instagram")
        Facebook = request.POST.get("Facebook")
        user_bio = request.POST.get("user_bio")
        user_fname = request.POST.get("fname")
        user_lname = request.POST.get("lname")
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        # try:
        event_user=Event_Users(user_fname=user_fname, user_lname=user_lname,username=username)
        event_user.save()
        print("this is evnt users",event_user.pk)
        social_media=Event_Socials(twitter=twitter,Facebook=Facebook,instagram=instagram,user_bio=user_bio,phone=phone,email=email)
        social_media.save()
        event_create=Event(event_name=event_name, event_location=event_location, event_org=event_org,event_start_date=event_start_date, event_end_date=event_end_date, event_image = fs.url(media_name) if event_img != False else "", host_id=event_user.pk)
        event_create.save()
        event_host=Event_Host(host_id=event_user.user_id, social_id=social_media.social_id,event_id=event_create.pk)
        event_host.save()
        messages.success(request, "Data Save Successfully")
        return HttpResponseRedirect(reverse("home-page"))
        # except:
        #     messages.error(request,"Error in Saving Data")
        #     return HttpResponseRedirect(reverse("home-page"))


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