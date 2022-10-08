from django import forms
from .models import *

class AddDonateForm(forms.Form):

    choices = [
        ('coins', 'Coins'),
        ('matic', 'Matic'),
    ]

    valuta = forms.MultipleChoiceField(choices=choices)
    value = forms.FloatField()