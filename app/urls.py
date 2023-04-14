from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receipt-upload', views.updateReceipt, name='receipt-upload'),
    path('appointments', views.appointments, name='appointments'),
    path('track-order', views.track, name='track-order'),
    path('testimonials', views.testimonials, name='testimonials')
    
    ]
