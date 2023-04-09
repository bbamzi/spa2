from django.contrib import admin

from .models import *

class paymentAdmin(admin.ModelAdmin):
    model= PaymentDetail

class bookingAdmin(admin.ModelAdmin):
    model= Booking
   


# Register your models here.
admin.site.register(PaymentDetail, paymentAdmin)
admin.site.register(Booking, bookingAdmin)