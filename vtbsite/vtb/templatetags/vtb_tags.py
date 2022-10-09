from django import template
from django.db.models import Q

from vtb.models import *

register = template.Library()

@register.simple_tag()
def get_guild_users(guild_id):
    guild_users = GuildUsers.objects.filter(guild_id=guild_id)
    return guild_users

@register.simple_tag()
def get_user_guilds(user_id):
    user_guilds = GuildUsers.objects.filter(guild_user_id=user_id)
    return user_guilds

@register.simple_tag()
def get_user(guild_user_id):
    user = Users.objects.get(id=guild_user_id)
    return user

@register.simple_tag()
def get_guild(guild_id):
    guild = Guilds.objects.get(id=guild_id)
    print(guild)
    return guild

@register.simple_tag()
def get_guilds(guild_user_id):
    user_guilds = GuildUsers.objects.filter(guild_user_id=guild_user_id)
    return user_guilds

@register.simple_tag()
def get_user_items(user_id):
    user_items = Inventory.objects.filter(user_id=user_id)
    return user_items

@register.simple_tag()
def get_item(item_id):
    item = Goods.objects.get(id=item_id)
    return item

@register.simple_tag()
def get_tasks_guilds(user_id):
    myuser = Users.objects.get(user_id=user_id)
    user_guilds = get_user_guilds(myuser.id)
    return user_guilds

@register.simple_tag()
def get_any_tasks():
    tasks = Tasks.objects.filter(for_guild__isnull=True)
    return tasks

@register.simple_tag()
def get_tasks(guild_id):
    tasks = Tasks.objects.filter(for_guild=guild_id)
    return tasks
