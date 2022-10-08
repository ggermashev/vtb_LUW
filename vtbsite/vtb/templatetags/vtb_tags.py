from django import template
from vtb.models import *

register = template.Library()

@register.simple_tag()
def get_guild_users(guild_id):
    guild_users = GuildUsers.objects.filter(guild_id=guild_id)
    return guild_users

@register.simple_tag()
def get_user(guild_user_id):
    user = Users.objects.get(id=guild_user_id)
    return user

@register.simple_tag()
def get_guild(guild_id):
    guild = Guilds.objects.get(id=guild_id)
    return guild

@register.simple_tag()
def get_guilds(guild_user_id):
    user_guilds = GuildUsers.objects.filter(guild_user_id=guild_user_id)
    return user_guilds