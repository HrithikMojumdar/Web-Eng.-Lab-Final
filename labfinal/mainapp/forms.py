from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import *


class userProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class RegistrationForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

class product_insert(forms.ModelForm):
    class Meta:
        model = product
        exclude  = ('seller',)