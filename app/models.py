from django.db import models

# Create your models here.
class Bookings(models.Model):
    name =  models.CharField(max_length=100, blank=True, null=True)
    email =  models.CharField(max_length=100, blank=True, null=True)
    date =  models.CharField(max_length=100, blank=True, null=True)
    time =  models.CharField(max_length=100, blank=True, null=True)
    service =  models.CharField(max_length=100, blank=True, null=True)
    payment_method =  models.CharField(max_length=100, blank=True, null=True)
    service_type =  models.CharField(max_length=100, blank=True, null=True)
    durations =  models.CharField(max_length=100, blank=True, null=True)
    receipt =  models.CharField(max_length=100, blank=True, null=True)
    


    def __str__(self) -> str:
        return f'order id: {self.id}'