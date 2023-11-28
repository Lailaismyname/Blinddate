from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non-Binary'),
        ('all', 'All')
    ]
    profile_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userprofile")
    date = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(validators=[
            MinValueValidator(0, message="Age must be at least 0."),
            MaxValueValidator(99, message="Age must be at most 99."),
        ])
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    looking_for_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    about_me = models.TextField(max_length=1500)
    interests = models.TextField(max_length=150, blank=True, null=True)
    hobbys = models.TextField(max_length=150, blank=True, null=True)
    user_foto = models.ImageField(upload_to="profileImages/", blank=True, null=True)

    def __str__(self):
        return f"{self.profile_owner}"
    


class Match(models.Model):
    match_list_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matchlist", null=True, blank=True)
    matches = models.ManyToManyField(Profile, related_name="matchlist")
    not_match_but_seen = models.ManyToManyField(Profile, related_name="not_match_but_seen", blank=True)
    def __str__(self):
        return f"Matches for {self.match_list_owner}"

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.OneToOneField(User, on_delete=models.CASCADE, related_name="chat_sender", blank=True, null=True)
    receiver = models.OneToOneField(User, on_delete=models.CASCADE, related_name="chat_receiver", blank=True, null=True)
    def __str__(self):
        return f"msg from {self.sender} to {self.receiver}"
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chat_message")
    message = models.TextField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.chat}, {self.message}"