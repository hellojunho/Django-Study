from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("AAA") 
    return render(request, 'stocks/home.html') 

def main(request):
    # return HttpResponse("Hello World")
    return render(request, 'stocks/home.html')