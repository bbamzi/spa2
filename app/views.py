from django.shortcuts import render

# Create your views here.
def index(request):

     return render(request, 'index.html',{"hello": "world"})

def appointments(request):

     return render(request, 'appointment.html',{"hello": "world"})


def opening(request):

     return render(request, 'opening.html',{"hello": "world"})

def testimonials(request):

     return render(request, 'testimonial.html',{"hello": "world"})