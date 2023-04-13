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
from django.template.loader import render_to_string
import smtplib
from email.message import EmailMessage



def send_email(message,email):

  smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
  smtp.login( os.getenv("sender"), os.getenv("password"))
  msg = EmailMessage()
  msg['Subject'] ='Your Invoice'
  msg['From'] = 'Invoice'
  msg['To']=email
  msg.set_content('Your Invoice')
  msg.add_alternative(message,subtype='html')
  smtp.send_message(msg)
  print('sent')

def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:ID_LENGTH]
# Create your views here.
def index(request):
     lst_payments = PaymentDetail.objects.all()
     return render(request, 'index.html',{"hello": "world","payment_types":lst_payments})

def appointments(request):
     lst_payments = PaymentDetail.objects.all()
   
     gen_id  = id_gen()
     if request.method == 'POST':

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
          
          
          # order_details = Booking.objects.get(order_id =gen_id )
          resp = {"order_id":gen_id,"payment_details":details.payment_value}
          html_message = render_to_string(
            "email_receipt.html",
            context={"order_id":gen_id,
                     "today":datetime.today().date,
                     "payment":request.POST.get('payment_method', None),
                     "service_type":request.POST.get('service_type', None),
                     "email":request.POST.get('email',"None"),
                     "order_status":"Awaiting_payment",
                     "name":request.POST.get('name'),
                     "client_address":request.POST.get('address', None),
                     "service":request.POST.get('service', None),
                     "total":request.POST.get('total', None),
                     "details":details.payment_value
                     },
        )
          
          # send_email(html_message,request.POST.get('email',"None"))
          return JsonResponse(resp)
         

     
     return render(request, 'appointment.html',{"hello": "world", "order_id":gen_id,"payment_types":lst_payments})


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
          # order.save()
                    

          return JsonResponse({"status":"success"})


def opening(request):

     return render(request, 'opening.html',{"hello": "world"})

def testimonials(request):

     return render(request, 'testimonial.html',{"hello": "world"})