from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import Http404
# Forms 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# Models
from .models import User, Profile


# Create your amazing views here.
def login_view(request):
    #if user is already logged in redirect to home page
    if request.user.is_authenticated:
        return redirect("index")
    else:
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

@login_required(login_url='login') 
def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    #if user is already logged in redirect to home page
    if request.user.is_authenticated:
        return redirect("index")
    else:
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


# View for the homepage
@login_required(login_url='login') 
def index(request):
    ...
    context = {}
    return render(request,"index.html",context)


#  View for the Profile page 
@login_required(login_url='login') 
def profile(request,profile_id):
    try:
        profile_owner = Profile.objects.get(pk=profile_id)
        print(profile_owner)
        context={
            "profile" : profile_owner
        }
        return render(request,"profile.html",context)
    except: 
        raise Http404("This profile does not exist.")


#  View for the Edit Profile page 
@login_required(login_url='login') 
def edit_profile(request):
    context={}
    return render(request,"editProfile.html",context)


#  View for the Find love page 
@login_required(login_url='login') 
def find_love(request):
    context={}
    return render(request,"findLove.html",context)


#  View for the Matches page 
@login_required(login_url='login') 
def matches(request):
    context={}
    return render(request,"matches.html",context)


#  View for the Chats page 
@login_required(login_url='login') 
def chats(request):
    context={}
    return render(request,"chats.html",context)


#  View for the individual Chat page 
@login_required(login_url='login') 
def individual_chat(request):
    context={}
    return render(request,"individualChat.html",context)