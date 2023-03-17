from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookingForm
from .models import Booking
from django.urls import reverse_lazy

# Create your views here.


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking:booking-create')