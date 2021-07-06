from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

#UserCreationForm is a built in django function for a user register form
# so users can log into the site

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


