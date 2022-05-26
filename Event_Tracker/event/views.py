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
from rest_framework import viewsets,generics,status      
from .models import Event, Event_Socials, Event_Users, Event_Host
from .models import Todo  
from .Event_forms import NameForm,SocialForm
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
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

    # event_list = Event.objects.all()
    # event_host = Event_Host.objects.all()
    event_join = Event_Host.objects.select_related('host','social','event').filter(auth_user=user.id)
    context = {
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user,
        'event_join': event_join
    }



    return render(request, "event/home.html",context)


def home_save_form(request):
    
    user = request.user

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
        about_event = request.POST.get("about_event")
        event_start_date = request.POST.get("event_start_date")
        event_end_date = request.POST.get("event_end_date")
        twitter = request.POST.get("twitter")
        instagram = request.POST.get("instagram")
        Facebook = request.POST.get("facebook")
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
        event_create=Event(event_name=event_name, event_location=event_location, event_org=event_org,event_start_date=event_start_date, event_end_date=event_end_date, event_image = fs.url(media_name) if event_img != False else "", about_event = about_event, host_id=event_user.pk)
        event_create.save()
        event_host=Event_Host(host_id=event_user.user_id, social_id=social_media.social_id,event_id=event_create.pk, auth_user = user.id)
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

def create(request):
    user = request.user

    auth0_user = user.social_auth.get(provider='auth0')

    user_data={
        'user_id':auth0_user.uid,
        'name':user.first_name,
        'picture':auth0_user.extra_data['picture']
    }

    return render(request,"event/create.html")



def man_event(request):
    user = request.user
    event_list = Event_Host.objects.select_related('host','social','event').filter(auth_user=user.id)
    
    return render(request, "event/man_event.html", {'event_list': event_list})

def event_entree(request):
    user = request.user
    
    return render(request, "event/event_entree.html",)

def delete_event(request, event_idd):
    # event = Event_Host.objects.select_related('host','social','event').filter(event_id=event_idd)
    event = Event.objects.get(pk=event_idd) 
    event.delete()
    return redirect("man_event")

def update_event_form(request, event_idd):
    
    user = request.user

    context = {}
    if request.method!="POST":
        return HttpResponseRedirect(reverse("man_event"))
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
        about_event = request.POST.get("about_event")
        event_start_date = request.POST.get("event_start_date")
        event_end_date = request.POST.get("event_end_date")
        twitter = request.POST.get("twitter")
        instagram = request.POST.get("instagram")
        Facebook = request.POST.get("facebook")
        user_bio = request.POST.get("user_bio")
        user_fname = request.POST.get("fname")
        user_lname = request.POST.get("lname")
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        # try:
        # event = Event_Host.objects.select_related('host','social','event').filter(event_id=event_idd).update(host_id=event_user.user_id, social_id=social_media.social_id,event_id=event_create.pk, auth_user = user.id)
        
        # eventt = Event.objects.filter('host', 'event_social').update_or_create()
        
        event_user=Event_Users.objects.filter(user_id=event_idd).update_or_create(user_fname=user_fname, user_lname=user_lname,username=username)
        # event_user.save()
        # print("this is evnt users",event_user.pk)
        social_media=Event_Socials.objects.filter(user_id=event_idd).update_or_create(twitter=twitter,Facebook=Facebook,instagram=instagram,user_bio=user_bio,phone=phone,email=email)
        # social_media.save()
        event_create=Event.objects.filter(event_id=event_idd).update_or_create(event_name=event_name, event_location=event_location, event_org=event_org,event_start_date=event_start_date, event_end_date=event_end_date, event_image = fs.url(media_name) if event_img != False else "", about_event = about_event)
        # event_create.save()
        # event_host=Event_Host.objects.update_or_create(host_id=event_user.user_id, social_id=social_media.social_id,event_id=event_create.pk, auth_user = user.id)
        # event_host.save()
        messages.success(request, "Data Save Successfully")
        return HttpResponseRedirect(reverse("man_event"))
        # except:
        #     messages.error(request,"Error in Saving Data")
        #     return HttpResponseRedirect(reverse("home-page"))


def update_event(request, event_idd):
        
    # event = Event_Host.objects.get(pk=event_id)
    event = Event_Host.objects.select_related('host','social','event').filter(event_id=event_idd)
    return render(request, "event/update_event.html", {'event': event})
    

def logout(request):
    django_logout(request)

    domain=config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to='http://127.0.0.1:8000/host'

    return HttpResponseRedirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all()  