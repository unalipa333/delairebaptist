from django.db import models
from django.contrib.auth.models import User


 
 # A model is the single, definitive source of information about your data. 
 # It contains the essential fields and behaviors of the data you're storing. 
 # Generally, each model maps to a single database table.
 
 # When you create a model, 
 # Django executes SQL to create a corresponding table in the database without you having to write a single line of SQL.






# extend the user model to have more fields
# this makes one profile pic to one user 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

        
