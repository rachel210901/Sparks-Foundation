from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *

from django.contrib.auth.decorators import login_required
import json
import datetime
import requests
from django.contrib.auth.models import User, auth


def index(request):
    return render(request, 'index')


def home(request):
    return render(request, 'index.html')


def cust(request):
    customer = Customer.objects.all()
    j = 'null'
    if request.method == "POST":
        email = request.POST['email']
        amt = request.POST['amount']
        rec = request.POST['rec']

        print(email)
        print(amt)
        print(rec)
        amt = int(amt)

        if email == 'select' or rec == 'select' or (email == 'select' and rec == 'select') or rec == email:
            messages.warning(
                request, "EmailId not selected or both EmailId's are same")
        elif amt <= 0:
            messages.warning(request, 'Please provide valid money details!!')
        else:
            for c in customer:
                if c.email == email:
                    j = email
                    i = c.id
                    name = c.name
                    if amt > c.accbal:
                        messages.warning(request, "Insufficient Balance!!")
                    break

        for x in customer:
            if x.email == rec:
                rid = x.id
                rname = x.name
                rbal = x.accbal
                break

        for c in customer:
            if c.email == email and rec != email and rec != 'select' and amt <= c.accbal and amt > 0:
                q1 = Transfer(sender=name, receiver=rname, amount=amt)
                accbal = c.accbal-amt
                q2 = Customer.objects.filter(id=i).update(accbal=accbal)
                q1.save()
                accbal = rbal+amt
                q3 = Customer.objects.filter(id=rid).update(accbal=accbal)
                messages.success(request, "Transfer complete!!")

    return render(request, 'transfermoney.html', {'customer': customer})


def transfer(request):
    tr = Transfer.objects.all()
    return render(request, 'transfer.html', {'tr': tr})


def cdetails(request):
    customer = Customer.objects.all()
    return render(request, 'customers.html', {'customer': customer})
