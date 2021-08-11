from django.db import models
from django.contrib.auth.models import User
from PIL import Image   #this allows us to resize profile image. the library is PIL


 
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


    def save(self):      #this gets run after the model is saved. It already exists in our parent class but we want to overide it. 
        super().save()   #super runs the save method of our parent class

        img = Image.open(self.image.path) #this opens the image of the current instance

        if img.height > 200 or img.width > 200:   #compares img height and width
            output_size = (100,100)                #tuple variable    
            img.thumbnail(output_size)              # resizes img
            img.save(self.image.path)               #saves img with new sizing



        
