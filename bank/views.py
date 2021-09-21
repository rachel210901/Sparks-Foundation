from django.shortcuts import render
from.models import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def customer(request):
    return render(request, "customer.html")

# Create your views here.
