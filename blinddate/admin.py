from django.contrib import admin
from .models import Profile, User, Match, Chat, Message

# Models To read ID
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

# Register your models here.
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Match)
admin.site.register(Chat)
admin.site.register(Message)
# admin.site.register()
