from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,HttpResponse, HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import Http404,HttpResponseForbidden, JsonResponse
from django.views.decorators.http import require_POST
# Forms 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, ProfileForm, MessageForm
# Models
from .models import User, Profile, Match, Chat, Message
# for chaining: 
from itertools import chain


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
            except ValueError as err:
                print(err)

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
def profile(request, user_id):
    try:
        # Check if user exists
        user = get_object_or_404(User, id=user_id)
        try:
            profile = get_object_or_404(Profile, profile_owner=user)
            # Check if user_foto exists in profile
            hasProfileFoto = bool(profile.user_foto)
        except Profile.DoesNotExist:
            return redirect('create_profile', user_id=user_id)
        context = {
            "profile": profile,
            "usermodel": user,
            "hasProfileFoto" : hasProfileFoto
        }
        return render(request, "profile.html", context)
    except Http404 as err:
        return redirect('create_profile', user_id=user_id)
    except Exception as err:
        raise Http404("Oops something went wrong, ", err) from err


#  View for the Edit Profile page 
@login_required(login_url='login') 
def edit_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = get_object_or_404(Profile, profile_owner=user)
    profile_picture = bool(profile.user_foto)
    # Check if the logged-in user is the owner of the profile
    if request.user != profile.profile_owner:
        return HttpResponseForbidden("You don't have permission to edit this profile.")
    user = User.objects.get(username=profile.profile_owner)
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            # route to pic /static/media/profileImages/
            print(request.FILES)
            profile = profile_form.save(commit=False)
            profile.save()
            return redirect('profile', user_id=user_id)
        else:
            print(profile_form.errors)
    else:
        profile_form = ProfileForm(instance=profile)
    context = {
        "user" : user,
        "profile" : profile,
        "profile_form" : profile_form,
        "profile_picture" : profile_picture
    }
    return render(request, "editProfile.html", context)


# View to create the profile for the user
@login_required(login_url='login') 
def create_profile(request,user_id):
    user = User.objects.get(id=user_id)
    create_form = ProfileForm()
    if request.method == "POST":
        create_form = ProfileForm(request.POST, request.FILES)
        if create_form.is_valid():
            profile = create_form.save(commit=False)
            print(request.user, profile.profile_owner)
            # check if the user creating the profile is also the user that is logged in.
            if request.user != profile.profile_owner:
                return HttpResponseForbidden("You don't have permission to edit this profile.")
            profile.save()
            return redirect('profile', user_id=user_id)
    context = {
        "user": user,
        "create_form" : create_form
    }
    return render(request, "createProfile.html", context)


#  View for the Find love page 
@login_required(login_url='login') 
def find_love(request):
    try:
        # get all the necesary data surrounding the profiles. 
        profiles = Profile.objects.all()
        user = request.user
        user_profile = Profile.objects.get(profile_owner=user)
        user_gender = user_profile.gender
        user_looking_for = user_profile.looking_for_gender
        match, created = Match.objects.get_or_create(match_list_owner=user)
        if created:
            pass

        filtered_profiles = []
        match_list = match.matches.all()
        seen_list = match.not_match_but_seen.all()
        for profile in profiles:
            # skip if its the users profile
            if profile == user_profile:
                continue
            # Check if profile has right gender, needs to be adjusted to take into account all preferences!!
            if profile.gender == user_looking_for:
            # check if profile is not already a match
                if profile not in match_list:
                    # and check if it is not already been seen
                    if profile not in seen_list:
                        filtered_profiles.append(profile)
            if user_looking_for == "all":
                if profile not in match_list:
                    # and check if it is not already been seen
                    if profile not in seen_list:
                        filtered_profiles.append(profile)
    except Profile.DoesNotExist:
        user_id = request.user.id
        print(user_id)
        return redirect("create_profile", user_id)
    #print(filtered_profiles)
    context = {
        "profiles": filtered_profiles,
        "matchlist" : match_list
    }
    return render(request, "findLove.html", context)

# View to make adjustments to Match
@login_required(login_url='login') 
def adjust_matchlist_no(request):
    if request.method == "POST":
        viewed_profile = request.POST.get("profile")
        logged_in_user = request.user
        match, created = Match.objects.get_or_create(match_list_owner=logged_in_user)
        if created:
            pass
        seen_list = match.not_match_but_seen.all()
        if viewed_profile not in seen_list:
            profile = Profile.objects.get(profile_owner=viewed_profile)
            match.not_match_but_seen.add(profile)
    return redirect('find_love')

@login_required(login_url='login') 
def adjust_matchlist_yes(request):
    if request.method == "POST":
        viewed_profile = request.POST.get("profile")
        logged_in_user = request.user
        match, created = Match.objects.get_or_create(match_list_owner=logged_in_user)
        if created:
            pass
        seen_list = match.matches.all()
        if viewed_profile not in seen_list:
            profile = Profile.objects.get(profile_owner=viewed_profile)
            match.matches.add(profile)
    return redirect('find_love')



#  View for the Matches page 
@login_required(login_url='login') 
def matches(request):
    logged_in_user = User.objects.get(username=request.user)
    match, created = Match.objects.get_or_create(match_list_owner=logged_in_user)
    if created:
        pass
    liked_profiles =  match.matches.all()
    matches = []
    for profile in liked_profiles:
        # get that users match list. Check if loggged in user is in matchlist
        profile_user = User.objects.get(username=profile)
        profile_match, created = Match.objects.get_or_create(match_list_owner=profile_user)
        for match in profile_match.matches.all():
            if str(match) == str(logged_in_user):
                matches.append(profile)
    context={
        "matches" : matches
    }
    return render(request,"matches.html",context)


#  View for the Chats page 
@login_required(login_url='login') 
def chat(request, match_name):
    msg_form = MessageForm()
    sender = request.user
    receiver = User.objects.get(username=match_name)
    match_profile = Profile.objects.get(profile_owner=receiver)
    # get chat if it exists
    sender_chat, created = Chat.objects.get_or_create(sender=sender, receiver=receiver)
    receiver_chat, created = Chat.objects.get_or_create(sender=receiver, receiver=sender)
    print(sender_chat)
    # get messages related to send_chat
    outgoing_messages = Message.objects.filter(chat=sender_chat)
    # get messages related to receiver_chat       
    incoming_messages = Message.objects.filter(chat=receiver_chat)
    all_messages = sorted(chain(outgoing_messages, incoming_messages), key=lambda message: message.timestamp)
    has_picture = bool(match_profile.user_foto)
    
    context={
        "match" : receiver,
        "match_profile" : match_profile,
        "has_picture": has_picture,
        "messages" : all_messages,
        "sender" : sender,
        "receiver": receiver,
        "msg_form": msg_form
    }
    return render(request,"chat.html",context)


#  View for sending Chats 
@login_required(login_url='login') 
def send_chat(request):
    if request.method == "POST":
        sender = request.user
        match = request.POST.get('receiver')
        receiver = User.objects.get(username=match)
        message = request.POST.get('message')
        chat, created = Chat.objects.get_or_create(sender=sender, receiver=receiver)
        message = Message(chat=chat, message=message)
        message.save()

    match_name = "peaches" 
    return redirect(f"chat/{match_name}")



# View to fetch profiles, in order to be able to render it with Javascript
@login_required(login_url='login') 
def fetch_profiles(request):
    profiles = list(Profile.objects.select_related('profile_owner').values('profile_owner__username','profile_owner_id', 'age', 'country', 'city', 'gender', 'looking_for_gender', 'about_me', 'interests', 'hobbys'))
    return JsonResponse(profiles, safe=False)
