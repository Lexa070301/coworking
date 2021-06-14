from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


class Payment(models.Model):
    date = models.DateTimeField('Дата оплаты', default='')
    size = models.IntegerField('Размер оплаты', default=0)
    booking = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.size)

    class Meta:
        verbose_name = 'Оплату'
        verbose_name_plural = 'Оплаты'


class Payment_status(models.Model):
    status = models.CharField('Статус', max_length=15, default='')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name = 'Статус оплыты'
        verbose_name_plural = 'Статусы оплат'
