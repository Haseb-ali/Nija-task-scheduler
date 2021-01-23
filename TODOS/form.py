from django import forms
from .models import TodoUserMedia


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        username = TodoUserMedia
        profile= ('username', 'profile')
