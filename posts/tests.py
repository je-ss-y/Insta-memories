from django.test import TestCase
from .models import Image,Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.

class ImageTestClass(TestCase):
# set up method
    def setUp(self):

        self.user=User.objects.create(username='jessy')
        # self.profile=Profile.objects.create(id=1,user=jessica,bio=creating,profile_photo="")
        self.image=Image(image='https://www.italymagazine.com/sites/default/files/styles/624xauto/public/feature-story/leader/bolzano-lead.jpg?itok=SsNNvkdk',photoname='person',caption='hello', pub_date='2019-9-2')

 #testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.image.Image))
        # self.assertTrue(isinstance(self.profile.Profile))
        self.assertTrue(isinstance(self.user.User))


    def save_instance(self):
        self.image.save_image()
        images=Image.objects.all()
        self .assertTrue(len(images)>0)

class ProfileClass(TestCase):
# set up method
    def setUp(self):

        self.profile=Profile.objects.create(id=1,user=jessica,bio=creating,profile_photo="https://www.italymagazine.com/sites/default/files/styles/624xauto/public/feature-story/leader/bolzano-lead.jpg?itok=SsNNvkdk")
        

 #testing instance 
    def test_instance(self):
       
        self.assertTrue(isinstance(self.profile.Profile))
     


    def save_instance(self):
        self.image.save_image()
        images=Image.objects.all()
        self .assertTrue(len(images)>0)

