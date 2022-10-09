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
    path('guild/<int:guild_id>', guild, name='guild'),
    path('guilds/', GuildsView.as_view(), name='guilds'),
    path('wallet/<int:user_id>', wallet, name='wallet'),
    path('choose_donation/<int:user_id>', donate_to_users, name='choose_donation'),
    path('donate/<int:from_id>/<int:to_id>', donate, name='donate'),
    path('inventory/<int:user_id>', inventory, name='inventory'),
    path('buying_coins/<int:item_id>/<int:user_id>', buying_coins, name='buying_coins'),
    path('buying_nft/<int:item_id>/<int:user_id>', buying_nft, name='buying_nft'),
    path('user_guilds/<int:user_id>', user_guilds, name='user_guilds'),
    path('join_guild/<int:guild_id>/<int:user_id>', join_guild, name='join_guild'),
    path('leave_guild/<int:guild_id>/<int:user_id>', leave_guild, name='leave_guild'),
    path('create_taks/', CreateTask.as_view(), name='create_task'),
]

