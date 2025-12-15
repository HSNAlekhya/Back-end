from django import forms
from django.contrib.auth.models import User
from .models import Player, Stadium, Profile

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        # fields = ['name', 'age', 'role', 'franchise']

class StadiumForm(forms.ModelForm):

    class Meta:
        model = Stadium
        fields = '__all__'

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'profile_picture']