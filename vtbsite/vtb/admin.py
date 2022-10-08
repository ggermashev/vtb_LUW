from django.contrib import admin
from .models import *


admin.site.register(Users)

admin.site.register(Roles)

admin.site.register(Goods)

admin.site.register(Categories)

admin.site.register(Events)

admin.site.register(Tasks)

admin.site.register(TaskFilters)

admin.site.register(News)