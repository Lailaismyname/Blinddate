from django.contrib import admin
from .models import Profile, User

# Models To read ID
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

# Register your models here.
admin.site.register(Profile,ProfileAdmin)
# admin.site.register()
