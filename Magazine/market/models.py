from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    sl = 'SL'
    cm = 'CM'

    role_choices = {
        sl : 'Продавец',
        cm : 'Покупатель'
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    user_avatar = models.ImageField(upload_to='avatars/', default='avatars\\Login_default_Avatar.png', blank=True, null=True)
    user_role = models.CharField(choices=role_choices, max_length=3)

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    # category = models.CharField()
    count = models.IntegerField()
    rating = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.SET_NULL)
    # photos
    # razmer
    price = models.FloatField()