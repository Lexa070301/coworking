from django.db import models

class Booking(models.Model):
    start_date = models.DateTimeField('Дата начала брони')
    end_date = models.DateTimeField('Дата окончания брони')
    def __str__(self):
        return self.start_date

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронирования'

class Booking_status(models.Model):
    status = models.CharField('Статус', max_length=15)
    payment = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус бронирования'
        verbose_name_plural = 'Статусы бронирований'