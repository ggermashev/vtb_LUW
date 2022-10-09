from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    firstname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    role = models.ForeignKey('Roles', on_delete=models.PROTECT, null=True)
    privateKey = models.CharField(max_length=128, null=True)
    publicKey = models.CharField(max_length=128, null=True)


    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.user.id})

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

class Friends(models.Model):
    user1 = models.ForeignKey('Users', related_name='User1', on_delete=models.PROTECT, null=True)
    user2 = models.ForeignKey('Users',related_name='User2', on_delete=models.PROTECT, null=True)

class Roles(models.Model):
    role = models.CharField(max_length=64, db_index=True)

    class Meta:
        verbose_name = 'Роли'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.role

class Goods(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.id})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class Categories(models.Model):
    category = models.CharField(max_length=64, db_index=True)

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.category

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

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=256, null=True)
    reward = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    for_guild = models.ForeignKey('Guilds', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'

class TaskFilters(models.Model):
    filter = models.CharField(max_length=64, db_index=True)

    class Meta:
        verbose_name = 'Фильтры заданий'
        verbose_name_plural = 'Фильтры заданий'

    def __str__(self):
        return self.filter


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

class Guilds(models.Model):
    guildName = models.CharField(max_length=16, db_index=True)
    description =models.CharField(max_length=128, null=True)
    guildPoints = models.IntegerField()
    guildRanking = models.CharField(max_length=4)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)

    def get_absolute_url(self):
        return reverse('guild', kwargs={'guild_id': self.id})

    def __str__(self):
        return self.guildName

    class Meta:
        verbose_name = 'Гальдии'
        verbose_name_plural = 'Гильдии'

class GuildUsers(models.Model):
    guild_user_id = models.ForeignKey('Users', on_delete=models.PROTECT, null=True)
    guild_id = models.ForeignKey('Guilds', on_delete=models.PROTECT, null=True)


class Inventory(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
    good_id = models.ForeignKey('Goods', on_delete=models.CASCADE, null=True)
    total_cost = models.IntegerField(null=True)