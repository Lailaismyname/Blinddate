from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("edit_profile/<int:user_id>", views.edit_profile, name="edit_profile"),
    path("create_profile/<int:user_id>", views.create_profile, name="create_profile"),
    path("find_love", views.find_love, name="find_love"),
    path("matches", views.matches, name="matches"),
    path("chat/<str:match_name>", views.chat, name="chat"),
    path("send_chat", views.send_chat, name="send_chat"),

    # for fetch requests:
    path("fetch_profiles", views.fetch_profiles, name="fetch_profiles"),
    path("adjust_matchlist_no", views.adjust_matchlist_no, name="adjust_matchlist_no"),
    path("adjust_matchlist_yes", views.adjust_matchlist_yes, name="adjust_matchlist_yes"),
]

# path("", views., name=""),