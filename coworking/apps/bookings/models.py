from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    start_date = models.DateTimeField('Дата начала брони')
    end_date = models.DateTimeField('Дата окончания брони')
    space = models.ForeignKey('spaces.Space', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.space) + ': ' + 'Начало: ' + str(self.start_date) + ' Конец: ' + str(
            self.end_date) + ' Пользователь: ' + str(self.user)

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронирования'


class Booking_status(models.Model):
    status = models.CharField('Статус', max_length=15)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.booking) + ' Статус: ' + str(self.status)

    class Meta:
        verbose_name = 'Статус бронирования'
        verbose_name_plural = 'Статусы бронирований'
