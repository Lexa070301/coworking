from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .forms import BookingUpdateForm, BookingCreateForm
from .models import Booking, Booking_status
from .serializers import BookingSerializer, Booking_statusSerializer


def index(request):
    bookings = Booking.objects.all().order_by('start_date')
    data = {
        'bookings': bookings,
        # 'features': features
    }
    return render(request, 'cabinet/bookings.html', data)

# def delete(request):
#     bookings = Booking.objects.all()
#     # features = Feature.objects.all()
#     data = {
#         'bookings': bookings,
#         # 'features': features
#     }
#     return render(request, 'cabinet/bookings.html', data)

class BookingsDeleteView(DeleteView):
    model = Booking
    success_url = '/bookings/'
    template_name = 'cabinet/bookings-delete.html'
    context_object_name = 'bookings'

class BookingsUpdateView(UpdateView):
    model = Booking
    success_url = '/bookings/'
    template_name = 'cabinet/bookings-update.html'
    form_class = BookingUpdateForm
    context_object_name = 'bookings'

class BookingsCreateView(CreateView):
    model = Booking
    success_url = '/bookings/'
    template_name = 'cabinet/bookings-create.html'
    form_class = BookingCreateForm
    context_object_name = 'bookings'

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.user = self.request.user
        # app_model.user = User.objects.get(user=self.request.user) # Or explicit model
        # Booking.save()
        return super().form_valid(form)


class BookingView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class SingleBookingView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class Booking_statusView(ListCreateAPIView):
    queryset = Booking_status.objects.all()
    serializer_class = Booking_statusSerializer


class SingleBooking_statusView(RetrieveUpdateDestroyAPIView):
    queryset = Booking_status.objects.all()
    serializer_class = Booking_statusSerializer