from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    sl = 'SL' #seller
    cm = 'CM' #customer

    ml = 'ml' #male
    fm = 'fm' #female

    role_choices = {
        sl : 'Продавец',
        cm : 'Покупатель',
    }

    gender_choices = {
        ml:'Мужской',
        fm:'Женский ',
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    user_avatar = models.ImageField(upload_to='avatars/', default='avatars\\Login_default_Avatar.png', blank=True, null=True)
    user_role = models.CharField(choices=role_choices, max_length=3)
    adress = models.TextField()
    phone_number = PhoneNumberField()
    gender = models.CharField(choices=gender_choices, max_length=3)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name', 'username']

class Product(models.Model):
    cl = 'cl' #clothes
    sh = 'sh' #shoes
    hm = 'hm' #home
    bt = 'bt' #beauty
    ac = 'ac' #accessories
    el = 'el' #electronics
    st = 'st' #sport
    ag = 'ag' #auto goods
    bk = 'bk' #books

    category_choices = {
        cl:'Одежда',
        sh:'Обувь',
        hm:'Дом',
        bt:'Красота',
        ac:'Аксессуары',
        el:'Электронника',
        st:'Спорт',
        ag:'Автотовары',
        bk:'Книги ',
    }

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(choices=category_choices, max_length=3)
    count = models.IntegerField()
    rating = models.FloatField(blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photos/')
