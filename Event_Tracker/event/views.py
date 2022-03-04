from django.shortcuts import redirect, render
from flask import request
import json

# Create your views here.
def start_page(request):
    user = request.user
    if user.is_authenticated:
        return redirect(home_page)
    else:
        return render(request, "event/index.html")

def home_page(request):
    return render(request, "event/home.html")

