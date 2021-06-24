from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField('Номер телефона', max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'