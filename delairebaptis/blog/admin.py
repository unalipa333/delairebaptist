from django.contrib import admin
from .models import Post

# This is where we can register our models so that they show up on our admin page

admin.site.register(Post)
