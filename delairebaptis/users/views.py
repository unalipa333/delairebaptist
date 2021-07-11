from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
#UserCreationForm is a built in django function for a user register form
# so users can log into the site

def register(request):
    if request.method== 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('blog-home')

    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


#one time alerts
# message.debug  message.info  message.success  message.warning   message.error



