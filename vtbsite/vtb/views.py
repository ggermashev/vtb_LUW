from django import forms
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView

from vtb.forms import *
from vtb.models import *

import sqlite3
import requests

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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'vtb/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('main')

def logout_user(request):
    logout(request)
    return redirect('main')

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
            r = requests.post("https://hackathon.lsp.team/hk/v1/wallets/new", data={}).json()
            print(r)
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            pubkey = r['publicKey']
            privkey = r['privateKey']
            cursor.execute(f"UPDATE vtb_users SET user_id='{user_id}' WHERE firstname='{form.cleaned_data['firstname']}' AND name='{form.cleaned_data['name']}' AND lastname='{form.cleaned_data['lastname']}'")
            cursor.execute(f"UPDATE vtb_users SET publicKey='{pubkey}' WHERE firstname='{form.cleaned_data['firstname']}' AND name='{form.cleaned_data['name']}' AND lastname='{form.cleaned_data['lastname']}'")
            cursor.execute(f"UPDATE vtb_users SET privateKey='{privkey}' WHERE firstname='{form.cleaned_data['firstname']}' AND name='{form.cleaned_data['name']}' AND lastname='{form.cleaned_data['lastname']}'")
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('login')
    else:
        form = FillInformationForm()
    return render(request, 'vtb/fill_information.html', {'form': form})


def main(request):
    return render(request, 'vtb/mainpage.html', {'menu': menu})

menu = [
    {'title': 'Главная', 'url': 'main'},
    {"title": "Магазин", 'url': 'goods'},
    {'title': 'Задания', 'url': 'tasks'},
    {'title': 'Гильдии', 'url': 'guilds'},
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class GuildsView(ListView):
    model = Guilds
    template_name = 'vtb/guilds.html'
    context_object_name = 'guilds'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

def guild(request, guild_id):
    myguild = Guilds.objects.get(id=guild_id)
    return render(request, 'vtb/guild.html', {'menu': menu, 'myguild': myguild})

def user_guilds(request, user_id):
    myuser = Users.objects.get(id=user_id)

    return render(request, 'vtb/user_guilds.html', {'menu': menu, 'myuser': myuser})

def profile(request, user_id):
    myuser = Users.objects.get(user_id=user_id)

    # r = requests.get(f"https://hackathon.lsp.team/hk/v1/wallets/{myuser.publicKey}/balance").json()
    # maticAmount = r['maticAmount']
    # coinsAmount = r['coinsAmount']
    # r = requests.get(f"https://hackathon.lsp.team/hk/v1/wallets/{myuser.publicKey}/nft/balance").json()

    return render(request, 'vtb/profile.html', {'menu': menu, 'myuser': myuser})

def wallet(request, user_id):
    myuser = Users.objects.get(id=user_id)
    r = requests.get(f"https://hackathon.lsp.team/hk/v1/wallets/{myuser.publicKey}/balance").json()
    maticAmount = r['maticAmount']
    coinsAmount = r['coinsAmount']
    r = requests.get(f"https://hackathon.lsp.team/hk/v1/wallets/{myuser.publicKey}/nft/balance").json()

    return render(request, 'vtb/wallet.html', {'menu': menu, 'myuser': myuser, 'maticAmount': maticAmount, 'coinsAmount': coinsAmount})

def donate(request, from_id, to_id):
    user_from = Users.objects.get(id=from_id)
    user_to = Users.objects.get(id=to_id)
    fromPrivateKey = user_from.privateKey
    toPublicKey = user_to.publicKey
    if request.method == 'POST':
        form = AddDonateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            headers = {'Content-type': 'application/json'}
            if form.cleaned_data['valuta'] == ['coins']:
                amount = form.cleaned_data['value']
                r = requests.post(f"https://hackathon.lsp.team/hk/v1/transfers/ruble", json={'fromPrivateKey': fromPrivateKey, 'toPublicKey': toPublicKey, 'amount': amount}, headers=headers).json()
                print(r)
            elif form.cleaned_data['valuta'] == ['matic']:
                amount = form.cleaned_data['value']
                r = requests.post(f"https://hackathon.lsp.team/hk/v1/transfers/matic", json={'fromPrivateKey': fromPrivateKey, 'toPublicKey': toPublicKey, "amount": amount}, headers=headers).json()
                print(r)
    else:
        form = AddDonateForm()
    return render(request, 'vtb/donate.html', {'menu': menu, 'form': form})

def donate_to_users(request, user_id):
    users = Users.objects.filter(~Q(id=user_id))

    return render(request, 'vtb/donate_to_users.html', {'menu': menu, 'users': users, 'from_id': user_id})

def inventory(request, user_id):
    myuser = Users.objects.get(id=user_id)
    return render(request, 'vtb/inventory.html', {'menu': menu, 'myuser': myuser, 'user_id': user_id})


def buying(request, item_id, user_id):

    myuser = Users.objects.get(user_id=user_id)
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO vtb_inventory (user_id_id, good_id_id) VALUES ('{myuser.id}', '{item_id}')")
    conn.commit()
    cursor.close()
    conn.close()


def buying_coins(request, item_id, user_id):
    buying(request, item_id, user_id)
    myuser = Users.objects.get(user_id=user_id)
    adm = User.objects.get(is_superuser=1)
    admin = Users.objects.get(user_id=adm.id)
    item = Goods.objects.get(id=item_id)
    headers = {'Content-type': 'application/json'}
    r = requests.post("https://hackathon.lsp.team/hk/v1/transfers/ruble", json={'fromPrivateKey': myuser.privateKey, 'toPublicKey': admin.publicKey, 'amount': item.price}, headers=headers).json()
    print(r)
    return redirect('goods')

def buying_nft(request, item_id, user_id):
    buying(request, item_id, user_id)
    return redirect('goods')