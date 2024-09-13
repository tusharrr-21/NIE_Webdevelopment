from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def service(request):
    return render(request,'service.html')

def contacts(request):
    return render(request,'contacts.html')


def basic(request):
    return render(request,'basic.html')