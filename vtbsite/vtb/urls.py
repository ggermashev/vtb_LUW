from django.urls import path
from vtb.views import *

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('', main, name='main'),
    path('fill_information/<slug:_username>/', fill_information, name='fill_information'),
    path('goods/', Store.as_view(), name='goods'),
    path('events/', Events.as_view(), name='events'),
    path('money/', Vallet.as_view(), name='vallet'),
    path('abilities/', Abilities.as_view(), name='abilities'),
    path('tasks/', Tasks.as_view(), name='tasks'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('guild/', Guild.as_view(), name='guild')
]

