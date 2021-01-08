from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Payment, Payment_status
from .serializers import PaymentSerializer, Payment_statusSerializer


def index(request):
    return HttpResponse('Payments works!')


class PaymentView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class SinglePaymentView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class Payment_statusView(ListCreateAPIView):
    queryset = Payment_status.objects.all()
    serializer_class = Payment_statusSerializer


class SinglePayment_statusView(RetrieveUpdateDestroyAPIView):
    queryset = Payment_status.objects.all()
    serializer_class = Payment_statusSerializer
