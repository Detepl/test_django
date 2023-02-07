from django.shortcuts import render
from .models import User
# Create your views here.


def index(request):
    users = User.objects.all()
    return render(request, "main/index.html",{"users":users})


def test(request):
    return render(request, "main/test.html")