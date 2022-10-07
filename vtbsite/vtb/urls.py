from django.urls import path
from vtb.views import *

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('', main, name='main'),
    path('fill_information/<slug:_username>/', fill_information, name='fill_information'),
]

