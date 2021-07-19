from django.db.models.signals import post_save
from django.contrib.auth.models import User  #sender.
from django.dispatch import receiver #receiver. is what receives the signal
from .models import Profile


# this is to create a profile for every new user
# this function runs everytime a user is created 

@receiver(post_save, sender=User) #this is a decorator, the signal is post_save
def create_profile(sender, instance, created, **kwargs): #the receiver is the create_profile function
    if created:
        Profile.objects.create(user=instance)


#saves profile everytime a user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()