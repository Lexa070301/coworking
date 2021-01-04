from django.db import models

class User(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    email = models.CharField('Email пользователя', max_length=50)
    phone_number = models.CharField('Телефон пользователя', max_length=15)
    def __str__(self):
        return self.name

class UserType(models.Model):
    type_name = models.CharField('Тип пользователя', max_length=15)
    access_level = models.IntegerField('Уровень доступа')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_name