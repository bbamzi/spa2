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
  smtp.login(os.getenv("sender"), os.getenv("password"))
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
     # print(request.get_host())
     
     try:
          active_address = ActiveAddress.objects.all()[0]
          address = HostingAddress.objects.get(state = active_address)
     except Exception:
          address = ""
     testimonies = Testimonial.objects.all()
     lst_payments = PaymentDetail.objects.all()
     return render(request, 'index.html',{"hello": "world","payment_types":lst_payments,"testimonies": testimonies, "address":address})




def appointments(request):
     lst_payments = PaymentDetail.objects.all()
     try:
          active_address = ActiveAddress.objects.all().first
          address = HostingAddress.objects.get(state = active_address)
     except Exception:
          address = ""
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
          order_time = datetime.now().time(),
          order_status = "Awaiting Payment"
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
                     "order_status":"Awaiting Payment",
                     "name":request.POST.get('name'),
                     "client_address":request.POST.get('address', None),
                     "service":request.POST.get('service', None),
                     "total":request.POST.get('total', None),
                     "details":details.payment_value
                    
                     },
        )
          
          send_email(html_message,request.POST.get('email',"None"))
          return JsonResponse(resp)
         

     
     return render(request, 'appointment.html',{"hello": "world", "order_id":gen_id,"payment_types":lst_payments, "address":address,})


def updateReceipt(request):
     if request.method == 'POST':
          
          id = request.POST.get('order_id', None)
          order = Booking.objects.get(order_id=id)
          file = request.FILES.get('file')
          extension = os.path.splitext(str(request.FILES.get('file')))[1]
          fss = FileSystemStorage()
          filename = fss.save(f'{id}{extension}', file)
          url = fss.url(filename)[6:]
          order.receipt = url
          order.order_status = "Confirming Payment"
          order.save()
          current_ip = f'{request.get_host()}/media{url}'
          print(current_ip)
          html_message = render_to_string(
            "receipt_upload.html",
            context={"order_id":id,
                     "name":order.name,
                     "link":current_ip
                     },
        ) 
          send_email(html_message,os.getenv("sender"))
          # send_email(html_message,os.getenv("sender"))
          print("sent")
                    

          return JsonResponse({"status":"success"})
     

def cancel_order(request):


     if request.method == "POST":
          id = request.POST.get('order_id', None)
          order = Booking.objects.get(order_id=id)
          order.order_status = request.POST.get('order_status', None)
          order.save()
          html_message = render_to_string(
            "cancel_order.html",
            context={"order_id":id,
                     "name":order.name
                     },
        ) 
          send_email(html_message,os.getenv("sender"))
          print("sent")
          return JsonResponse({"status":"success"})



def track(request):
     try:
          active_address = ActiveAddress.objects.all().first
          address = HostingAddress.objects.get(state = active_address)
     except Exception:
          address = ""
     if request.method == 'POST':
          id = request.POST.get('tracking_id', None)
          email = request.POST.get('email', None)
          try:
               order = Booking.objects.get(order_id=id, email=email)
               data= {
                    "status_code":200,
                    "order_id":order.order_id,
                     "date":order.order_date,
                     "name":order.name,
                     "order_time":order.order_time,
                     "payment_method":order.payment_method,
                     "service_type":order.service_type,
                     "email":order.email,
                     "order_status":order.order_status,
                     "client_address":order.client_address,
                     "service":order.service,
                     "total":order.total
                     }
               return JsonResponse(data)
          except Exception as e:
               print(e)
               return JsonResponse({"status_code":404})

     return render(request, 'track.html',{"hello": "world", "address":address})

def testimonials(request):
     testimonies = Testimonial.objects.all()
     try:
          active_address = ActiveAddress.objects.all().first
          address = HostingAddress.objects.get(state = active_address)
     except Exception:
          address = ""
     return render(request, 'testimonial.html',{"testimonies": testimonies, "address":address,})