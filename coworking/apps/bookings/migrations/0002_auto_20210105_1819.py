# Generated by Django 3.1.4 on 2021-01-05 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_status',
            old_name='payment',
            new_name='booking',
        ),
    ]
