from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.Main, name='Main'),
    path('flights/', views.Flights, name='Flights'),
    path('hotels/', views.Hotels, name='Hotels'),
    path('trains/', views.Trains, name='Trains'),
    path('buses/', views.Buses, name='Buses'),
    path('card/', views.Card, name='Card'),
    path('aboutus/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('payment/', views.Payment, name='Payment'),
    path('ticket/', views.Ticket, name='Ticket'),
    path('myaccount/', views.Account, name='Account'),
    path('paymentmode/', views.Mode, name='Mode'),
    path('mypayments/', views.Mypay, name='Mypay'),
    path('netpay/', views.Netpay, name='Netpay'),
    path('mytrains/', views.Mytrain, name='Mytrain'),
    path('mybuses/', views.Mybus, name='Mybus'),
    path('myhotels/', views.Myhotel, name='Myhotel'),
    path('suggestions/', views.Suggestion, name='Suggestion'),
    path('weight/', views.Weight, name='Weight')
]