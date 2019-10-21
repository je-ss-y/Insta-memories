from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class Image(models.Model):
    image=  models.ImageField(upload_to='images/', blank=True)
    photoname = models.TextField()
    caption = HTMLField()
    # upvote = models.ManyToManyField(User)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    # tags = models.ManyToManyField(tags)


    def __str__(self):
        return self.photoname

    @classmethod
    def search_by_name(cls,search_term):
        user = cls.objects.filter(user__username__contains=search_term)
        return user
    
    @classmethod
    def get_image(cls):
        image= cls.objects.all().prefetch_related('comment_set')
        return image
    

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField()
    profilepicture= models.ImageField(upload_to='profile/', blank=True)


    def __str__(self):
        return self.profilepicture




class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment












  
