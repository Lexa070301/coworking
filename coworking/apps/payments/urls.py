from django.urls import path
from . import views
from .views import PaymentView, SinglePaymentView, Payment_statusView, SinglePayment_statusView

app_name = "payments"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.index, name='index'),
    path('api/payments', PaymentView.as_view()),
    path('api/payments/<int:pk>', SinglePaymentView.as_view()),
    path('api/payment_status', Payment_statusView.as_view()),
    path('api/payment_status/<int:pk>', SinglePayment_statusView.as_view())
]
