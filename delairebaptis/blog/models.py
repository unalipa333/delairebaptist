from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#This is creating what the Django database will hold for blog posts


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):     #dunder method (double underscore method) having post printed out by title
        return self.title 