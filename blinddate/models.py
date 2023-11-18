from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non-Binary'),
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
    user_foto = models.ImageField(upload_to="blinddate/static/media/profileImages/", blank=True, null=True)



    def __str__(self):
        return f"{self.profile_owner}"