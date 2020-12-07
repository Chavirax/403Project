from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexPageView(request):
    return render(request, 'parking/index.html')

def aboutPageView(request) :

    context = {
      
        "places_to_park" : ["U Lots", "Y Lots", "A Lots","C Lots"]
    } 

    return render(request, 'parking/about.html', context) 

def contactPageView(request, contact_name, contact_email):
    return HttpResponse('Welcome ' + contact_name + "! We will send an email to " + contact_email)

def registerPageView(request):
    return HttpResponse("This is where you register your vehicle.")

def loginPageView(request):
    return HttpResponse("This is where you log in to our system.")


