from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
{
    'author': 'lyndon',
    'title': 'blog post',
    'date': 'today'

}

]



def home(request):
    context = { 
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')


