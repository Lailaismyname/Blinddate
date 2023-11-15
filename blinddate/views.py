from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect,HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Forms 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


# Create your amazing views here.
def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        # check if user is authenticated
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request,"username/password is incorrect")
            return render(request,"login.html",context)
    return render(request,"login.html",context)


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    err_msg = None
    form = RegisterForm
    if request.method == "POST":
        try:
            form = RegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("login")
        except ValueError:
            err = ValueError

    context = {
        "form": form,
        "err_msg": err_msg
    }
    return render(request,"register.html",context)


def index(request):
    ...
    context = {}
    return render(request,"index.html",context)
