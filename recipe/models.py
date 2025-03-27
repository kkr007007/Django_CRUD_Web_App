from django.db import models

class recipe(models.Model):

    recipe_name=models.CharField(max_length=200)
    recipe_description=models.TextField()
    image=models.ImageField(upload_to='recipe_img')
    
    
