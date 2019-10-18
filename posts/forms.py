from .models import Image
from django import forms




class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }