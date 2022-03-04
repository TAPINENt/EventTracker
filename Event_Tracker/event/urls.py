from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.start_page, name = "start-page"),
    path("home", views.home_page, name="home-page"),
    path("", include('social_django.urls')),
    # path("login", views.login_page, name="login-page"),
    # path("signup", views.login_page, name="login-page"),
]