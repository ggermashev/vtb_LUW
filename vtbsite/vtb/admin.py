from django.contrib import admin
from .models import *


admin.site.register(Users)

admin.site.register(Roles)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'photo')


admin.site.register(Goods, GoodsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)

admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Events)

admin.site.register(Tasks)

admin.site.register(TaskFilters)

admin.site.register(News)