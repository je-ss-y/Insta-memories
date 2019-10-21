from django.db import models
from .models import Image,Profile,Comment
from django import forms
from django.contrib.auth.models import User




class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['editor', 'pub_date']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        bio = models.TextField()
        profilepicture= models.ImageField(upload_to='images/', blank=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
      



       