from django.db import models

class Payment(models.Model):
    date = models.DateTimeField('Дата оплаты')
    size = models.IntegerField('Размер оплаты')
    booking = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE)
    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Оплату'
        verbose_name_plural = 'Оплаты'

class Payment_status(models.Model):
    status = models.CharField('Статус', max_length=15)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус оплыты'
        verbose_name_plural = 'Статусы оплат'