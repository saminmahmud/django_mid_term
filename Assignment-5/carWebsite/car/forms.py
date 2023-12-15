from django import forms
from .models import Car, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class CarForm(forms.ModelForm):  
    class Meta:
        model = Car
        fields = "__all__"
    
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'body']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' , 'email']

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
