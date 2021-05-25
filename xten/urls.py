from django.urls import path
from . import views
urlpatterns = [
   
    path('paris/', views.Paris, name='Paris'),
    path('agra/', views.Agra, name='Agra'),
    path('barcelona/', views.Barcelona, name='Barcelona'),
    path('delhi/', views.Delhi, name='Delhi'),
    path('dubai/', views.Dubai, name='Dubai'),
    path('goa/', views.Goa, name='Goa'),
    path('hyderabad/', views.Hyderabad, name='Hyderabad'),
    path('kerala/', views.Kerala, name='Kerala'),
    path('kolkata/', views.Kolkata, name='Kolkata'),
    path('losangeles/', views.Losangeles, name='Losangeles'),
    path('moscow/', views.Moscow, name='Moscow'),
    path('mumbai/', views.Mumbai, name='Mumbai'),
    path('mysore/', views.Mysore, name='Mysore'),
    path('newyork/', views.Newyork, name='Newyork'),
    path('singapore/', views.Singapore, name='Singapore'),
    path('tokyo/', views.Tokyo, name='Tokyo'),
    path('booking/', views.Booking, name='Booking'),
    path('events/', views.Events, name='Events')
]