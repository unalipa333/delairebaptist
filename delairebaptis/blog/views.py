from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.



#the home function is going to handle the traffic from the home page of the blog
# this will control what the user sees. note the html file.  

def home(request):
    context = { 
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# the about function is going to handle the traffic from the about page of the blog
# note the html file

@login_required()
def about(request):
    return render(request, 'blog/about.html', {'title': 'About}'})


