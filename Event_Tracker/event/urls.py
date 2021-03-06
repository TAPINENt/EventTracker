from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from tomlkit import document
from . import views
from .views import RoomView, JoinEvent,GetEvent

# app_name = 'event'

router = routers.DefaultRouter()                   
router.register(r'todos', views.TodoView, 'todo') 

urlpatterns = [
    path('api/', include(router.urls)),
    path("", views.start_page, name = "start-page"),
    path("event/home/", views.home_page, name="home-page"),
    path("home_save_form", views.home_save_form, name="home-save-form"),
    path("update_event_form/<event_idd>", views.update_event_form, name="update_event_form"),
    path("delete_event/<event_idd>", views.delete_event, name="delete_event"),
    path("event/profile/", views.profile, name="profile"),
    path("event/create/", views.create, name="create"),
    path("event_entree", views.event_entree, name="event_entree"),
    path("event/update_event/<event_idd>", views.update_event, name="update_event"),
    path("event_entree/<str:event_code>", views.event_entree, name="event_entree"),
    path("event/man_event/", views.man_event, name="man_event"),
    path("event/api/", RoomView.as_view()),
    path("join-event", JoinEvent.as_view()),
    path("get-event", GetEvent.as_view()),
    path("", include('social_django.urls')),
    path("logout/",views.logout,name="logout"),
    # path("login", views.login_page, name="login-page"),
    # path("signup", views.login_page, name="login-page"),
]

