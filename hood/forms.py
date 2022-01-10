from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email', 'neighbourhood',]

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'neighbourhood']

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model=NeighbourHood
        fields = ['hood_image','name','hood_description','location']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title','post_image','post_description','hood',]

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields = ['name','business_photo','description','location', 'neighborhood']
        