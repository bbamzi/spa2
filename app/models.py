from django.db import models
import uuid
from django.utils.http import int_to_base36

# Create your models here.

ID_LENGTH = 9


def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:ID_LENGTH]
class Bookings(models.Model):
    order_id = models.CharField(max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False)
    order_date = models.DateField(auto_now_add=True)
    order_time =models.TimeField(auto_now=False, auto_now_add=False)
    name =  models.CharField(max_length=100, blank=True, null=True)
    email =  models.CharField(max_length=100, blank=True, null=True)
    date =  models.CharField(max_length=100, blank=True, null=True)
    time =  models.CharField(max_length=100, blank=True, null=True)
    service =  models.CharField(max_length=100, blank=True, null=True)
    payment_method =  models.CharField(max_length=100, blank=True, null=True)
    service_type =  models.CharField(max_length=100, blank=True, null=True)
    durations =  models.CharField(max_length=100, blank=True, null=True)
    total =  models.CharField(max_length=100, blank=True, null=True)
    receipt =  models.CharField(max_length=100, blank=True, null=True)



    def __str__(self) -> str:
        return f'order id: {self.id}'
    
    
    class PaymentDetails(models.Model):
        cashApp =  models.CharField(max_length=100, blank=True, null=True)
        venmo =  models.CharField(max_length=100, blank=True, null=True)
        paypal =  models.CharField(max_length=100, blank=True, null=True)
        bitcoin =  models.CharField(max_length=100, blank=True, null=True)
        zelle =  models.CharField(max_length=100, blank=True, null=True)
        

