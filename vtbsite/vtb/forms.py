from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class FillInformationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstname', 'name', 'lastname']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'lastname': forms.TextInput(attrs={'class': 'form-input'}),
        }

class AddDonateForm(forms.Form):

    choices = [
        ('coins', 'Coins'),
        ('matic', 'Matic'),
    ]

    valuta = forms.MultipleChoiceField(choices=choices)
    value = forms.FloatField()

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'reward', 'photo', 'for_guild']
