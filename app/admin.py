from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, Solicitation, Post

# Register your models here.
admin.site.register(Profile, UserAdmin)
admin.site.register(Solicitation)
admin.site.register(Post)
