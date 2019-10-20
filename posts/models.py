from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class Image(models.Model):
    image=  models.ImageField(upload_to='images/', blank=True)
    photoname = models.TextField()
    caption = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    # tags = models.ManyToManyField(tags)


    def __str__(self):
        return self.photoname

    @classmethod
    def search_by_name(cls,search_term):
        user = cls.objects.filter(user__contains=search_term)
        return user
    

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField()
    profilepicture= models.ImageField(upload_to='profile/', blank=True)


    def __str__(self):
        return self.profilepicture




# class Comment(models.Model):
#     comment = models.TextField()
#     image = models.ForeignKey(Image, on_delete=models.CASCADE)
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)


#     def __str__(self):
#         return f'{self.user.name} Image'












  
