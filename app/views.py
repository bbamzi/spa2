from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import *
import uuid
from django.utils.http import int_to_base36
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import base64
import os

def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:ID_LENGTH]
# Create your views here.
def index(request):

     return render(request, 'index.html',{"hello": "world"})

def appointments(request):
     if request.method == 'POST':
          gen_id  = id_gen()
          new_booking = Booking(
          order_id = gen_id,
          name = request.POST.get('name', 'N/A'),
          email=request.POST.get('email',"None"),
          date = request.POST.get('date', None),
          time = request.POST.get('time', None),
          service = request.POST.get('service', None),
          payment_method = request.POST.get('payment_method', None),
          service_type = request.POST.get('service_type', None),
          client_address = request.POST.get('address', None),
          client_phone_number = request.POST.get('phone_number', None),
          durations = request.POST.get('how_long', None),
          total = request.POST.get('total', None),
          receipt = request.POST.get('receipt', None),
          order_date = datetime.now().date(),
          order_time = datetime.now().time()
          )
          new_booking.save()
          details = PaymentDetail.objects.get(payment_type = request.POST.get('payment_method', None))
          resp = {"order_id":gen_id,"payment_details":details.payment_value}
          return JsonResponse(resp)
     
     return render(request, 'appointment.html',{"hello": "world", "order_id":gen_id})


def updateReceipt(request):
     if request.method == 'POST':
          
          id = request.POST.get('order_id', None)
          order = Booking.objects.get(order_id=id)
          file = request.FILES.get('file')
        
          extension = os.path.splitext(str(request.FILES.get('file')))[1]
        
          fss = FileSystemStorage()
          filename = fss.save(f'{id}.{extension}', file)
          url = fss.url(filename)
          order.receipt = url
          order.save()
                    

          return JsonResponse({"status":"success"})


def opening(request):

     return render(request, 'opening.html',{"hello": "world"})

def testimonials(request):

     return render(request, 'testimonial.html',{"hello": "world"})