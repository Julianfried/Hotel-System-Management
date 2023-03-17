from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'
    template_name: 'django/forms/widgets/date.html'
    input_formats = ['%d/%m/%Y']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {
            'guest_name' : forms.TextInput(attrs={'name' : 'guest_name','class' : 'form-control'}),
            'check_in' : DateInput( attrs={'type': 'date', 'name' : 'check_in', 'class' : 'form-control'}),
            'check_out' : DateInput(attrs={'type': 'date', 'name' : 'check_out', 'class' : 'form-control'}),
            'guest_email' : forms.EmailInput(attrs={'name' : 'guest_email', 'class' : 'form-control'}),
            'room' : forms.Select(attrs={'name' : 'room','class' : 'form-select'}),
            'pay_status' : forms.Select(attrs={'name' : 'pay_status','class' : 'form-select'}),
            'payment_method' : forms.Select(attrs={'name' : 'payment_method','class' : 'form-select'}),
            'tariff' : forms.NumberInput(attrs={'name' : 'tariff','class' : 'form-control'}),
        }
