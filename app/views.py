from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import *

# Create your views here.
def index(request):

     return render(request, 'index.html',{"hello": "world"})

def appointments(request):
     if request.method == 'POST':
          
          new_booking = Bookings(
          name = request.POST.get('name', 'N/A'),
          email=request.POST.get('email',"None"),
          date = request.POST.get('date', None),
          time = request.POST.get('time', None),
          service = request.POST.get('service', None),
          payment_method = request.POST.get('payment_method', None),
          service_type = request.POST.get('service_type', None),
          durations = request.POST.get('how_long', None),
          total = request.POST.get('total', None),
          receipt = request.POST.get('receipt', None),
          order_date = datetime.now().date(),
          order_time = datetime.now().time()
          )
          new_booking.save()
     
     return JsonResponse({"Wewe":"wewe"}, safe=False)

     


def opening(request):

     return render(request, 'opening.html',{"hello": "world"})

def testimonials(request):

     return render(request, 'testimonial.html',{"hello": "world"})