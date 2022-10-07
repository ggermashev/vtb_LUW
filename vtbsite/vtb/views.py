from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView

from vtb.models import *

import sqlite3

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

class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = 'vtb/registration.html'
    user_name = ''
    success_url = '/fill_information/{}'.format(user_name)

    def form_valid(self, form):
        self.object = form.save()
        self.user_name = form.cleaned_data['username']
        self.success_url = f"/fill_information/{self.user_name}"
        print(self.user_name)
        return HttpResponseRedirect(self.get_success_url())

class FillInformationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstname', 'name', 'lastname']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'lastname': forms.TextInput(attrs={'class': 'form-input'}),
        }

def fill_information(request, _username):
    if request.method == 'POST':
        form = FillInformationForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = User.objects.get(username=_username).id
            #Users.objects.raw(f"UPDATE vtb_users SET user_id={user_id} WHERE firstname={form.cleaned_data['firstname']} AND name={form.cleaned_data['name']} AND lastname={form.cleaned_data['lastname']}")
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM vtb_users")
            print(cursor.fetchall())
            cursor.execute(f"UPDATE vtb_users SET user_id='{user_id}' WHERE firstname='{form.cleaned_data['firstname']}' AND name='{form.cleaned_data['name']}' AND lastname='{form.cleaned_data['lastname']}'")
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('main')
    else:
        form = FillInformationForm()
    return render(request, 'vtb/fill_information.html', {'form': form})


def main(request):
    return HttpResponse("done")