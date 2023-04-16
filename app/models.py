from django.db import models
import uuid
from django.utils.http import int_to_base36

# Create your models here.

ID_LENGTH = 9


def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:ID_LENGTH]

society = ["Awaiting Payment","Confirming Payment","Payment Received","Order Completed","Order Cancelled"]

status_choices = ((i, i) for i in society)


class Booking(models.Model):
    order_id =  models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)
    order_time =models.TimeField(auto_now=False, auto_now_add=False)
    name =  models.CharField(max_length=100, blank=True, null=True)
    email =  models.CharField(max_length=100, blank=True, null=True)
    date =  models.CharField(max_length=100, blank=True, null=True)
    time =  models.CharField(max_length=100, blank=True, null=True)
    service =  models.CharField(max_length=100, blank=True, null=True)
    payment_method =  models.CharField(max_length=100, blank=True, null=True)
    service_type =  models.CharField(max_length=100, blank=True, null=True)
    client_address = models.CharField(max_length=1000,blank=True,null=True)
    client_phone_number = models.CharField(max_length=1000,blank=True,null=True)
    durations =  models.CharField(max_length=100, blank=True, null=True)
    total =  models.CharField(max_length=100, blank=True, null=True)
    receipt =  models.ImageField(null = True, blank=True ,upload_to= "images/")
    order_status =  models.CharField(max_length=100, choices=status_choices, blank=True, null=True)




    def __str__(self) -> str:
        return f'order--{self.order_id} created {self.order_date}'
    
    
class PaymentDetail(models.Model):
    payment_type =  models.CharField(max_length=100, blank=True, null=True)
    payment_value =  models.CharField(max_length=100, blank=True, null=True)
    payment_tag =  models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.payment_type}'
    

class HostingAddress(models.Model):
    address_nickname= models.CharField(max_length=1000, blank=True)
    state = models.CharField(max_length=1000, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    lat = models.CharField(max_length=1000, blank=True)
    lng= models.CharField(max_length=1000, blank=True)

    def __str__(self) -> str:
        return f'{self.address_nickname}'


class Testimonial(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    social_username = models.CharField(max_length=200,blank=True,null=True)
    social_network = models.CharField(max_length=200,blank=True,null=True)
    testimony = models.CharField(max_length=200,blank=True,null=True)
    ratings = models.IntegerField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)




   
# booking = HostingAddress.objects.all()
# state = [i.state for i in booking if booking]
# state_choices = ((i, i) for i in state)
        

class ActiveAddress(models.Model):
    address_nickname =  models.CharField(max_length=100,  blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.address_nickname}'

