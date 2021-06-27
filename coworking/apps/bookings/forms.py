from .models import Booking
from django.forms import ModelForm, DateInput, Select

class BookingUpdateForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['end_date']

        widgets = {
            "end_date": DateInput(attrs={
                "type": "date",
                "placeholder": "Дата",
                "value": Booking.end_date
            })
        }


class BookingCreateForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'space']

        widgets = {
            "start_date": DateInput(attrs={
                "type": "date",
                "placeholder": "Дата начала"
            }),
            "end_date": DateInput(attrs={
                "type": "date",
                "placeholder": "Дата окончания"
            }),
            "space": Select()
        }