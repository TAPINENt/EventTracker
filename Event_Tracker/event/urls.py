from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.start_page, name = "start-page"),
    path("home", views.home_page, name="home-page"),
    path("profile/", views.profile, name="profile"),
    path("", include('social_django.urls')),
    path('logout/',views.logout,name='logout'),
    # path("login", views.login_page, name="login-page"),
    # path("signup", views.login_page, name="login-page"),
]