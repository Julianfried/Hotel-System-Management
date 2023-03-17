from django.urls import path
from .views import BookingCreateView

app_name='booking'

urlpatterns = [
    
    path('booking-create/', BookingCreateView.as_view(), name = 'booking-create'),
]
