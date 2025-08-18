from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name="booking"),
    path('booking-success/', lambda request: render(request, 'booking_success.html'), name='booking_success')
]
