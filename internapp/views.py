from django.shortcuts import render
from django.http import HttpResponse

def coffee(request):
    #return HttpResponse("<h1>Hey there you are connected with the django server!!</h1>")
    return render (request, 'coffee.html')

def home(request):
    #return HttpResponse("One hello!!")
    return render (request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about_us.html')

def chocolate(request):
    return render(request, 'chocolate.html')