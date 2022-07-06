from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('join', index),
    path('create/', index),
    path('welcome/<str:eventCode>', index),
    path('event/<str:eventCode>', index)
]