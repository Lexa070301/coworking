from django.db import models
from django.contrib.auth.models import User

class Space(models.Model):
    address = models.CharField('Адрес', max_length=60)
    capacity = models.IntegerField('Вместимость')
    name = models.CharField('Название', max_length=30)
    area = models.IntegerField('Площадь')
    daily_cost = models.IntegerField('Цена за день')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пространство'
        verbose_name_plural = 'Пространства'


class Rating(models.Model):
    rating = models.IntegerField('Рейтинг')
    review = models.TextField('Отзыв')
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Feature(models.Model):
    feature = models.CharField('Фича', max_length=30)

    def __str__(self):
        return self.feature

    class Meta:
        verbose_name = 'Фичу'
        verbose_name_plural = 'Фичи'


class Space_feature(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    def __str__(self):
        return self.space

    class Meta:
        verbose_name = 'Пространство и фичу'
        verbose_name_plural = 'Пространства и фичи'
