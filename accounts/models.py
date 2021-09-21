from datetime import datetime, timezone, date
from os import name
from django.db import models
from django.db.models.fields import AutoField


class Customer(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    acct = models.IntegerField(default=0)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    accbal = models.IntegerField()


class Transfer(models.Model):
    sender = models.CharField(max_length=200, null=True)
    receiver = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(default=0)
    date_tran = models.DateTimeField(auto_now_add=True)
