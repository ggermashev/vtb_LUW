from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    firstname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    role = models.ForeignKey('Roles', on_delete=models.PROTECT, null=True)


class Friends(models.Model):
    user1 = models.ForeignKey('Users', related_name='User1', on_delete=models.PROTECT, null=True)
    user2 = models.ForeignKey('Users',related_name='User2', on_delete=models.PROTECT, null=True)

class Roles(models.Model):
    role = models.CharField(max_length=64)

class Goods(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

class Categories(models.Model):
    category = models.CharField(max_length=64)

