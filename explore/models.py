from django.db import models
from twilio.rest import Client
import random as rd
# Create your models here.
class Flight(models.Model):
    uname = models.CharField(max_length=20)
    ticketID = models.CharField(max_length=10)
    fNO = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    fdest = models.CharField(max_length = 30)
    tdest = models.CharField(max_length = 30)
    depart = models.CharField(max_length=30)
    retur = models.CharField(max_length=30)
    classi = models.CharField(max_length=20)
    passe = models.CharField(max_length=30)
    airline = models.CharField(max_length=30)
    price = models.CharField(max_length=10)

class Querie(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    country = models.CharField(max_length=20)
    subject = models.TextField()

class Pay(models.Model):
    uname = models.CharField(max_length=20)
    payID = models.CharField(max_length=15)
    fname = models.CharField(max_length=30)
    bank = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    amount = models.CharField(max_length=10)
    mob= models.CharField(max_length=15)
    def __str__(self):
        return str(self.amount)

    def save(self, *args, **kwargs):
        if self.amount:
            account_sid = 'ACef59812ce7df16710656ddfd9f24ab9e'
            auth_token = '1614fbfd81d24351d4b1a50d61de81cc'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                                        body=f'Dear {self.fname} OTP for Your Payment of {self.amount} is  {rd.randint(111111,999999)}',
                                        from_='+18055002173',
                                        to=f'+91{self.mob}'
                                    )

            print(message.sid)

        return super().save(*args, **kwargs)

class NetPay(models.Model):
    uname = models.CharField(max_length=20)
    payID = models.CharField(max_length=15)
    usr = models.CharField(max_length=30)
    bank = models.CharField(max_length=20)
    amount = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    mob = models.CharField(max_length=15)
    def __str__(self):
        return str(self.amount)

    def save(self, *args, **kwargs):
        if self.amount:
            account_sid = 'ACef59812ce7df16710656ddfd9f24ab9e'
            auth_token = '1614fbfd81d24351d4b1a50d61de81cc'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                                        body=f'Dear {self.usr} OTP for Your Net Banking Payment of {self.amount} is  {rd.randint(111111,999999)}',
                                        from_='+18055002173',
                                        to=f'+91{self.mob}'
                                    )

            print(message.sid)

        return super().save(*args, **kwargs)

class Hotel(models.Model):
    uname = models.CharField(max_length=20)
    bID = models.CharField(max_length=15)
    destination = models.CharField(max_length=30)
    checkin = models.CharField(max_length=20)
    checkout = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    rooms = models.CharField(max_length=10)
    adults = models.CharField(max_length=10)
    children = models.CharField(max_length=10)
    date = models.CharField(max_length=20)


class Train(models.Model):
    trname = models.CharField(max_length=20)
    trno = models.CharField(max_length=20)
    fromd = models.CharField(max_length=20)
    tod = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    clas = models.CharField(max_length=20)
    passe = models.CharField(max_length=5)
    uname= models.CharField(max_length=20)

class Bus(models.Model):
    uname= models.CharField(max_length=20)
    ticketID = models.CharField(max_length=20)
    fromd = models.CharField(max_length=20)
    tod = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    clas = models.CharField(max_length=20)
    passe = models.CharField(max_length=5)
    travel = models.CharField(max_length=30)
    