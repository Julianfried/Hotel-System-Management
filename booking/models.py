from django.db import models
# Create your models here.
ROOM_CATEGORIES = (
    ('FAM', 'FAMILY'),
    ('EJE', 'EJECUTIVO'),
    ('GRA', 'GRANDS'),
)


class Room(models.Model):
    number = models.IntegerField()
    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES)

    def __str__(self):
        return f'{self.number}'


class Booking(models.Model):
    PAYMENT_STATUSES = (
        ('COM', 'COMPLETO'),
        ('INC', 'INCOMPLETO'),
        ('PAR', 'PARCIAL'),
    )
    PAYMENT_METHODS = (
        ('DEB', 'DEBITO'),
        ('CRE', 'CREDITO'),
        ('EFE', 'EFECTIVO'),
        ('TRA', 'TRANSFERENCIA'),
    )
    guest_name = models.CharField(max_length=40, default="")
    guest_email = models.EmailField(max_length=200, default="")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    pay_status = models.CharField(
        max_length=3, choices=PAYMENT_STATUSES, default="")
    payment_method = models.CharField(
        max_length=15, choices=PAYMENT_METHODS, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    tariff = models.PositiveIntegerField()

    def __str__(self):
        return f'Desde {self.check_in} hasta = {self.check_out}'
