from django.db import models
from django.contrib.auth.models import AbstractUser

from products.models import DepositProducts, SavingProducts

# from allauth.account.utils import user_email, user_field, user_username


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True, default=0)
    salary = models.IntegerField(blank=True, null=True, default=0)
    interest = models.CharField(max_length=20, null=True)


    # 중개테이블 만들기
    user_deposit_products = models.ManyToManyField(DepositProducts)
    user_saving_products = models.ManyToManyField(SavingProducts)


    
    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

