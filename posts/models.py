from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Image(models.Model):
    image=  models.ImageField(upload_to='images/', blank=True)
    photoname = models.TextField()
    caption = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # tags = models.ManyToManyField(tags)


    def __str__(self):
        return self.photoname
    
  
