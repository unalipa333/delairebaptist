from django.contrib import admin
from .models import Profile


# Register your models here.
#allows admin to view user profiles on the admin page of the site

admin.site.register(Profile)


