from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()                   
router.register(r'todos', views.TodoView, 'todo') 

urlpatterns = [
    path('api/', include(router.urls)),
    path("", views.start_page, name = "start-page"),
    path("home", views.home_page, name="home-page"),
    path("home_save_form", views.home_save_form, name="home-save-form"),
    path("profile/", views.profile, name="profile"),
    path("", include('social_django.urls')),
    path('logout/',views.logout,name='logout'),
    # path("login", views.login_page, name="login-page"),
    # path("signup", views.login_page, name="login-page"),
]