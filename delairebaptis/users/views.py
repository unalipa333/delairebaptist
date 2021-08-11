from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
#UserCreationForm is a built in django function for a user register form
# so users can log into the site

def register(request):
    if request.method== 'POST':   #checks to see if the request type is a post
        form = UserRegisterForm(request.POST)
        if form.is_valid():         # if the form is valid
            form.save()             # then form is saved
            username = form.cleaned_data.get('username')  # grabs the username that was entered in the form
            messages.success(request, f'Your account has been created. You are now able to log in using {username}!') #displays message with new username that user created
            return redirect('login')

    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


#one time alerts
# message.debug  message.info  message.success  message.warning   message.error

#this is the profile section and what the user sees in that section. 
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #not passing anything in will leave the inside of the form fields blank. This will also instantiate the variable or activate it.
                                                        # Here I have passed the user data so that the form field will have the users current ID and we will know what user we are working with.  
                                                        # request.POST is the new data that the user may enter in order to update their profile
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # same comments as above. 
                                                                                # request.POST will update the profile image
        if u_form.is_valid() and p_form.is_valid():  #checks to see if the data that the user entered is valid
            u_form.save()                            # saves updated data
            p_form.save()                            # saves updated data
            messages.success(request, f'Your account has been updated!') #displays message 
            return redirect('profile')  #redirects to profile page in order to avoid post/get wierd message
    else:
        u_form = UserUpdateForm(instance=request.user) #not passing anything into it will leave the inside of the form fields blank. This will also instantiate the variable or activate it.
                                                        # Here I have passed the user data so that the form field will have the users current ID.   
        p_form = ProfileUpdateForm(instance=request.user.profile) # same comments as above. 

    context = {             #create dictionary with key value pairs in order to pass into return render
        'u_form' : u_form,
        'p_form' : p_form

    }
    return render(request, 'users/profile.html', context)