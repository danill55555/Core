from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    telephone = models.CharField(max_length=20, verbose_name='Телефон')


