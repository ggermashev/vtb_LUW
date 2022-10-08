from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView

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

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'vtb/login.html'

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
            cursor.execute(f"UPDATE vtb_users SET user_id='{user_id}' WHERE firstname='{form.cleaned_data['firstname']}' AND name='{form.cleaned_data['name']}' AND lastname='{form.cleaned_data['lastname']}'")
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('main')
    else:
        form = FillInformationForm()
    return render(request, 'vtb/fill_information.html', {'form': form})


def main(request):
    return render(request, 'vtb/mainpage.html', {'menu': menu})

menu = [
    {'title': 'Главная', 'url': 'main'},
    {"title": "Магазин", 'url': 'goods'},
    {"title": "События", 'url': 'events'},
    {'title': 'Задания', 'url': 'tasks'},
    #{"title": "Профиль", 'url': 'profile'},
    {'title': 'Регистрация', 'url': 'registration'},
    {'title': 'Вход', 'url': 'login'},
]

class Store(ListView):
    model = Goods
    template_name = 'vtb/store.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['filter'] = Categories.objects.all()
        return context

class Events(ListView):
    pass

class Vallet(ListView):
    pass

class Abilities(ListView):
    pass

class Tasks(ListView):
    model = Tasks
    template_name = 'vtb/tasks.html'
    context_object_name = 'tasks'


class Guild(ListView):
    model = Guild
    template_name = 'vtb/guild.html'
    context_object_name = 'guild'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


def profile(request, user_id):
    user = Users.objects.get(pk=user_id)
    return render(request, 'vtb/profile.html', {'menu': menu, 'user': user})
