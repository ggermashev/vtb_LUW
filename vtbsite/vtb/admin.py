from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'name', 'lastname')

admin.site.register(Users, UsersAdmin)

admin.site.register(Roles)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'photo')


admin.site.register(Goods, GoodsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)

admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Events)

class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'reward', )

admin.site.register(Tasks, TasksAdmin)

admin.site.register(TaskFilters)

admin.site.register(News)

class GuildsAdmin(admin.ModelAdmin):
    list_display = ('guildName', 'guildPoints', 'guildRanking', 'photo')

admin.site.register(Guilds, GuildsAdmin)

