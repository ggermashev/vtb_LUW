from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    firstname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    role = models.ForeignKey('Roles', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.user.id})

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

class Friends(models.Model):
    user1 = models.ForeignKey('Users', related_name='User1', on_delete=models.PROTECT, null=True)
    user2 = models.ForeignKey('Users',related_name='User2', on_delete=models.PROTECT, null=True)

class Roles(models.Model):
    role = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Роли'
        verbose_name_plural = 'Роли'

class Goods(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.id})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

class Categories(models.Model):
    category = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'

class Events(models.Model):
    creator = models.ForeignKey('Users', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    reward = models.IntegerField()

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_id': self.id})

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'


class Tasks(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    reward = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)
    min_exp = models.IntegerField()
    filter = models.ForeignKey('TaskFilters', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_id': self.id})

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'

class TaskFilters(models.Model):
    filter = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Фильтры заданий'
        verbose_name_plural = 'Фильтры заданий'


class News(models.Model):
    author = models.ForeignKey('Users', related_name='User', on_delete=models.PROTECT, null=True)
    header_news = models.CharField(max_length=64)
    content = models.CharField(max_length=512)
    time_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('piece_of_news', kwargs={'news_id': self.id})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['time_created']