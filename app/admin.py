from django.contrib import admin

# Register your models here.
from .models import Profile, Message, Post, Friendship

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Friendship)