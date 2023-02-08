from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.


def index(request):
    users = User.objects.all()
    return render(request, "main/index.html",{"users":users})


def test(request):
    return render(request, "main/test.html")

def add_user(request):
    error=""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
        else:
            error = "incorrect"


    form = UserForm()
    inf = {
        "form": form,
        'error':error
    }
    return render(request, "main/add_user.html", inf)