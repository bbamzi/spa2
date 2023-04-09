from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):

     return render(request, 'index.html',{"hello": "world"})

def appointments(request):
     
     name = request.GET.get('name', 'N/A')
     email=request.GET.get('email',"None")
     date = request.GET.get('date', None)
     time = request.GET.get('time', None)
     service = request.GET.get('service', None)
     payment_method = request.GET.get('payment_method', None)
     service_type = request.GET.get('service_type', None)
     durations = request.GET.get('durations', None)
     receipt = request.GET.get('receipt', None)
     
     return JsonResponse({"Wewe":"wewe"}, safe=False)

     


def opening(request):

     return render(request, 'opening.html',{"hello": "world"})

def testimonials(request):

     return render(request, 'testimonial.html',{"hello": "world"})