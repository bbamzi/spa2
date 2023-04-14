from django.contrib import admin

from .models import *

class paymentAdmin(admin.ModelAdmin):
    model= PaymentDetail
    list_display = ('payment_type', 'payment_value')

class bookingAdmin(admin.ModelAdmin):
    model= Booking
class HostingAdmin(admin.ModelAdmin):
    model= HostingAddress
    list_display = ('address_nickname', 'address',"state","city","zip","state")
   
class TestimonyAdmin(admin.ModelAdmin):
    model= Testimonial
    list_display = ('name', 'social_username',"social_network","testimony","ratings","url")
   


# Register your models here.
admin.site.register(PaymentDetail, paymentAdmin)
admin.site.register(Booking, bookingAdmin)
admin.site.register(HostingAddress, HostingAdmin)
admin.site.register(Testimonial, TestimonyAdmin)