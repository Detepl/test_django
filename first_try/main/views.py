from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>it_works???</h1>")


def test(request):
    return HttpResponse("<h1>it_really_works</h1>")