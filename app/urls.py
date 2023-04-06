from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointments', views.appointments, name='appointments'),
    path('openings', views.opening, name='opening'),
    path('testimonials', views.testimonials, name='testimonials')
    
    ]
