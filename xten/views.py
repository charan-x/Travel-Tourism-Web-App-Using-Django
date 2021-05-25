from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from xten.models import Review
# Create your views here.

def Paris(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Paris",review = review)
        ins.save()
    return render(request, 'paris.html')

def Hyderabad(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Hydearbad",review = review)
        ins.save()
    return render(request, 'hyderabad.html')

def Moscow(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Moscow",review = review)
        ins.save()
    return render(request, 'moscow.html')

def Agra(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Agra",review = review)
        ins.save()
    return render(request, 'agra.html')

def Delhi(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Delhi",review = review)
        ins.save()
    return render(request, 'delhi.html')

def Dubai(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Dubai",review = review)
        ins.save()
    return render(request, 'dubai.html')

def Goa(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Goa",review = review)
        ins.save()
    return render(request, 'goa.html')

def Mumbai(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Mumbai",review = review)
        ins.save()
    return render(request, 'mumbai.html')

def Mysore(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Mysore",review = review)
        ins.save()
    return render(request, 'mysore.html')

def Newyork(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "New York",review = review)
        ins.save()
    return render(request, 'newyork.html')

def Tokyo(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Tokyo",review = review)
        ins.save()
    return render(request, 'tokyo.html')

def Singapore(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Singapore",review = review)
        ins.save()
    return render(request, 'singapore.html')

def Kerala(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Kerala",review = review)
        ins.save()
    return render(request, 'kerala.html')

def Kolkata(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Kolkata",review = review)
        ins.save()
    return render(request, 'kolkata.html')

def Losangeles(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "LosAngeles",review = review)
        ins.save()
    return render(request, 'losangeles.html')

def Barcelona(request):
    if request.method == "POST":
        uname = request.user
        review = request.POST['review']
        ins = Review(uname=uname,placename = "Barcelona",review = review)
        ins.save()
    return render(request, 'barcelona.html')
    
def Booking(request):
    return render(request, 'booking.html')


@login_required(login_url='Login')
def Events(request):
    return render(request, 'event.html')