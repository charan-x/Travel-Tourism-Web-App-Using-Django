from re import sub
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from explore.models import Flight
from explore.models import Querie
from explore.models import Pay
from explore.models import NetPay
from explore.models import Hotel
from explore.models import Train
from explore.models import Bus
from django.core.mail import send_mail
import string
import random
import datetime
import json
# Create your views here.
def Main(request):
    return render(request, 'mainExplore.html')

@login_required(login_url='Login')
def Mybus(request):
    bus_info = Bus.objects.all()
    return render(request, 'mybuses.html',{'Buses':bus_info})

@login_required(login_url='Login')
def Myhotel(request):
    hotel_info = Hotel.objects.all()
    return render(request, 'myhotels.html',{'Hotels':hotel_info})

@login_required(login_url='Login')
def Flights(request):
    if request.method == "POST":
        N = 8
        uname = request.user
        ticketID = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
        num = random.randint(1111,9999)
        fNO=str(num)
        name = request.POST['name']
        fdest = request.POST['fdest']
        tdest = request.POST['tdest']
        depart = request.POST['depart']
        retur = request.POST['return']
        classi = request.POST['classi']
        passe = request.POST['passe']
        airline = request.POST['airline']
        price = str(random.randint(2000,7000))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        ins = Flight(uname=uname,ticketID=ticketID,fNO=fNO,name= name,fdest=fdest, date=date,tdest=tdest,depart=depart,retur=retur,classi=classi,passe=passe,airline=airline,price=price)
        ins.save()
        return redirect('/explore/paymentmode/')

    return render(request, 'Flights.html')

@login_required(login_url='Login')
def Mode(request):
    ticket_info= Flight.objects.all()
    return render(request, 'paymentmode.html')

@login_required(login_url='Login')
def Buses(request):
    if request.method == "POST":
        N = 8
        uname = request.user
        ticketID = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
        b = ["Morning Star Travels","Yatra Services","All India Travels","Southeren Travels","Orange Travels","SVR Travels","Seabird Travels","Kaveri Travels"]
        travel = random.choice(b)
        fromd = request.POST['fromd']
        tod = request.POST['tod']
        date = request.POST['date']
        clas = request.POST['clas']
        passe = request.POST['passe']
        ins = Bus(uname=uname,ticketID=ticketID,fromd=fromd,tod=tod,date=date,clas=clas,passe=passe,travel=travel)
        ins.save()
        return render(request, 'Buses.html',{'Travels':travel,'From':fromd,'To':tod})
        
    return render(request, 'Buses.html')

@login_required(login_url='Login')
def Mytrain(request):
    train_info = Train.objects.all()
    return render(request, 'mytrains.html',{'Trains':train_info})

@login_required(login_url='Login')
def Hotels(request):
    if request.method == "POST":
        N = 6
        uname = request.user
        bID = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
        destination = request.POST['destination']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        type = request.POST['type']
        rooms = request.POST['rooms']
        adults = request.POST['adults']
        children = request.POST['children']
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        ins = Hotel(uname=uname,bID=bID,destination=destination,checkin=checkin,checkout=checkout,type=type,rooms=rooms,adults=adults,children=children,date=date)
        ins.save()
        return redirect('/explore/paymentmode/')
    return render(request, 'Hotels.html')

@login_required(login_url='Login')
def Trains(request):
    if request.method == "POST":
        fromd = request.POST['fromd']
        tod = request.POST['tod']
        date = request.POST['date']
        clas = request.POST['clas']
        passe = request.POST['passe']
        uname = request.user

        if(fromd=="Hyderabad" and tod=="Mumbai"):
            trname = "Mumbai Express"
            trno = "17032"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Hyderabad" and tod=="Delhi"):
            trname = "Telengana Express"
            trno = "12723"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Hyderabad" and tod=="Kolkata"):
            trname = "Falaknuma Express"
            trno = "12704"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Hyderabad" and tod=="Kochi"):
            trname = "TVC FESTVL SPL"
            trno = "07230"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Hyderabad" and tod=="Agra"):
            trname = "HYB NDLS SPL"
            trno = "02723"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()
        
        elif(fromd=="Hyderabad" and tod=="Ahmedabad"):
            trname = "RJT FESTVL SPL"
            trno = "02756"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Vijayawada" and tod=="Mumbai"):
            trname = "BBS CSMT SPL"
            trno = "01020"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()
        
        elif(fromd=="Vijayawada" and tod=="Delhi"):
            trname = "VSKP NDLS SPL"
            trno = "02805"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Vijayawada" and tod=="Kolkata"):
            trname = "MAS HWH SPL"
            trno = "02822"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Vijayawada" and tod=="Kochi"):
            trname = "TATA ERS SPL"
            trno = "08189"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Vijayawada" and tod=="Agra"):
            trname = "MAS NDLS EXP"
            trno = "02615"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Vijayawada" and tod=="Ahmedabad"):
            trname = "PURI OKHA SPL"
            trno = "08401"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()
        
        elif(fromd=="Visakhapatnam" and tod=="Mumbai"):
            trname = "BBS CSMT SPL"
            trno = "01020"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Visakhapatnam" and tod=="Delhi"):
            trname = "VSKP NZM SPL"
            trno = "02851"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)                
            ins.save()

        elif(fromd=="Visakhapatnam" and tod=="Kolkata"):
            trname = "SC HWH SPL"
            trno = "02704"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Visakhapatnam" and tod=="Kochi"):
            trname = "DHN ALLP SPL"
            trno = "03351"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Visakhapatnam" and tod=="Agra"):
            trname = "VSKP NZM SPL"
            trno = "02851"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Visakhapatnam" and tod=="Ahmedabad"):
            trname = "VSKP GIMB SPL"
            trno = "08501"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Tirupati" and tod=="Mumbai"):
            trname = "MAS KDCY SF SPL"
            trno = "09119"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Tirupati" and tod=="Delhi"):
            trname = "TVC NDLC SF EXP"
            trno = "02625"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Tirupati" and tod=="Kolkata"):
            trname = "MYS HWH SPL"
            trno = "08118"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Tirupati" and tod=="Kochi"):
            trname = "NDLS TVC SF SPL"
            trno = "02626"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Tirupati" and tod=="Agra"):
            trname = "TVC NDLC SF EXP"
            trno = "02625"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        elif(fromd=="Tirupati" and tod=="Ahmedabad"):
            trname = "MAS ADI EXP"
            trno = "06051"
            ins = Train(fromd=fromd,tod=tod,date=date,clas=clas,trname=trname,trno=trno,passe=passe,uname=uname)
            ins.save()

        return render(request, 'Trains.html',{'Tno':trno,'Tname':trname,'From':fromd,'Tod':tod})

    return render(request, 'Trains.html')



def Card(request):
    return render(request, 'card.html')

def About(request):
    return render(request, 'aboutus.html')

def Contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        country = request.POST['country']
        subject = request.POST['subject']
        ins = Querie(name=name,email=email,subject=subject,country=country)
        ins.save()
    return render(request, 'contact.html')


@login_required(login_url='Login')
def Payment(request):
    price = str(random.randint(2000,7000))
    if request.method == "POST":
        N = 12
        payID = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
        uname = request.user
        fname = request.POST['fname']
        bank = request.POST['bank']
        amount = request.POST['amount']
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        mob = request.POST['mob']
        ins = Pay(uname=uname,payID=payID,fname=fname,bank=bank,date=date,amount=amount,mob=mob)
        ins.save()
        return render(request, 'payment.html',{'Mobile':mob,'Amount':amount,'Name':fname})

    return render(request, 'payment.html',{'Price':price})

@login_required(login_url='Login')
def Ticket(request):
    ticket_info= Flight.objects.all()
    usr = request.user
    return render(request, 'ticket.html',{'Tickets':ticket_info,'usrname':usr})
    
@login_required(login_url='Login')
def Account(request):
    return render(request, 'myaccount.html')

@login_required(login_url='Login')
def Netpay(request):
    price = str(random.randint(2000,7000))
    if request.method == "POST":
        N = 12
        payID = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
        uname = request.user
        usr = request.POST['usr']
        bank = request.POST['bank']
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        amount = request.POST['amount']
        mob = request.POST['mob']
        ins = NetPay(payID=payID,uname=uname,usr=usr,bank=bank,amount=amount,date=date,mob=mob)
        ins.save()
        return render(request, 'payment.html',{'Mobile':mob,'Amount':amount,'Name':uname})
    return render(request, 'netpay.html',{'Price1':price})
    
@login_required(login_url='Login')
def Mypay(request):
    payinfo = Pay.objects.all()
    payinfo2 = NetPay.objects.all()
    return render(request, 'mypayments.html',{'Payments':payinfo,'Netpays':payinfo2})

def Suggestion(request):
    if request.method == "POST":
        fromd = request.POST['fromd']
        tod = request.POST['tod']
        if  ((fromd=="Vijayawada" or fromd=="Hyderabad" or fromd=="Vizag" or fromd=="Chennai" or fromd=="Bangalore")and (tod=="Goa")):
            sug1 = "Goa !"
            sug2 = "Do not stick to the popular beaches"
            sug3 = "Practice caution at the Goa beaches"
            sug4 = "Savour Goan cuisine"
            sug5 = "Explore on two-wheels"
            sug6 = "Go beyond the sea and sand"
            sugd= "Distance is > 600 KM +"
            sug7 = "Better To Travel through Flight"
            sug8 = "Pack as less luggauge as possible so that You won't get into Trouble At the Airport"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6,'Sug7':sug7,'Sug8':sug8,'Sugd':sugd})
        
        elif  ((fromd=="Vijayawada" or fromd=="Hyderabad" or fromd=="Vizag" or fromd=="Chennai" or fromd=="Bangalore")and (tod=="Mumbai")):
            sug1 = "Mumbai !"
            sug2 = "Nightlife in Mumbai"
            sug3 = "Weekend getaways from Mumbai"
            sug4 = "Restaurants in Mumbai"
            sug5 = "Marine Drive – Take An Evening Walk"
            sug6 = "Bandstand – Watch The Sunset"
            sugd= "Distance is > 700 KM +"
            sug7 = "Better To Travel through Flight"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6,'Sugd':sugd,'Sug7':sug7})


        elif ((fromd == "Hyderabad" or fromd == "Vijayawada" or fromd == "Vizag" or fromd == "Chennai" or fromd == "Bangalore") and (tod =="Kolkata")):
            sug1 = "Kolkata !"
            sug2 = "Sundarbans – Admire Wildlife In Their Natural Habitat"
            sug3 = "Science City – Enhance Your Knowledge"
            sug4 = "Nicco Park – Have Some Fun Time"
            sug5 = "Park Street – Shop Your Heart Out"
            sug6 = "Princep Ghat – Watch The Sun Go Down"
            sugd= "Distance is > 1000 KM +"
            sug7 = "Better To Travel through Flight"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug7':sug7,'Sugd':sugd,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6})

        
        elif ((fromd == "Hyderabad" or fromd == "Vijayawada" or fromd == "Vizag" or fromd == "Chennai" or fromd == "Bangalore") and (tod =="Manali")):
            sug1 = "Manali !"
            sug2 = "Choose City Centre or Well connected Hotels,Resorts"
            sug3 = "Avoid Peak Times and Festivals for Himachal Trip"
            sug4 = "April to June is the best time to visit Manali"
            sug5 = "Favour Busy Dhabas and Restaurants"
            sug6 = "Nearest Airport is Shimlla Bhuntar Kullu"
            sugd= "Distance is > 1000 KM +"
            sug7 = "Better To Travel through Flight"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug7':sug7,'Sugd':sugd,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6})

        elif ((fromd=="Vijayawada" or fromd=="Hyderabad" or fromd=="Vizag" ) and (tod == "Mysore")):
            sug1 = "Mysore !"
            sug2 = "Mysore Palace – Admire The Grandeur"
            sug3 = "Karanji Lake – Soak Up Some Peace"
            sug4 = "Chamundeshwari Temple – Visit"
            sug5 = "3D Selfie Gallery – Capture Memories"
            sug6 = "KRS Dam – Explore"
            sugd= "Distance is > 750 KM +"
            sug7 = "Better To Travel through Flight Or Train"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug7':sug7,'Sugd':sugd,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6})

        elif ((fromd=="Bangalore" or fromd=="Chennai") and (tod == "Mysore")):
            sug1 = "Mysore !"
            sug2 = "Mysore Palace – Admire The Grandeur"
            sug3 = "Karanji Lake – Soak Up Some Peace"
            sug4 = "Chamundeshwari Temple – Visit"
            sug5 = "3D Selfie Gallery – Capture Memories"
            sug6 = "KRS Dam – Explore"
            sug7 = "Better To Travel through Train or Bus"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug7':sug7,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6})

        elif ((fromd=="Vijayawada" or fromd=="Hyderabad" or fromd=="Vizag" or fromd=="Chennai" ) and (tod == "Kerala")):
            sug1 = "Kerala !"
            sug2 = "Munnar – Watch The Neelakurinji Bloom"
            sug3 = "Alleppey – Stay In A Houseboat"
            sug4 = "Thekkady – Take A Spice Tour"
            sug5 = "Athirapally Falls – Get Drenched"
            sug6 = "Periyar Wildlife Sanctuary – Take A Jeep Ride"
            sugd= "Distance is > 900 KM +"
            sug7 = "Better To Travel through Flight or a Train"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug7':sug7,'Sugd':sugd,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6})

        elif (( fromd=="Bangalore" ) and (tod == "Kerala")):
            sug1 = "Kerala !"
            sug2 = "Munnar – Watch The Neelakurinji Bloom"
            sug3 = "Alleppey – Stay In A Houseboat"
            sug4 = "Thekkady – Take A Spice Tour"
            sug5 = "Athirapally Falls – Get Drenched"
            sug6 = "Periyar Wildlife Sanctuary – Take A Jeep Ride"
            sug7 = "Better To Travel through Train or a Bus"
            return render(request, 'suggestions.html',{'Sug1':sug1,'Sug7':sug7,'Sug2':sug2,'Sug3':sug3,'Sug4':sug4,'Sug5':sug5,'Sug6':sug6})

        else:
            sug1 = "Please Choose the Destination"
            return render(request, 'suggestions.html',{'Sug1':sug1})

    return render(request, 'suggestions.html')

def Weight(request):
    if request.method == "POST":
        weights = request.POST['weights']
        values = request.POST['values']
        classi = request.POST['classi']
        wt = list(weights.split(" "))
        
        for i in range(0, len(wt)):
            wt[i]= int(wt[i])
        val = list(values.split(" "))
        for i in range(0, len(val)):
            val[i]= int(val[i])
            
        total = sum(val)
        print(total)

        # KNAPSACK ALGORITHM
        
        def knapSack(W, wt, val, n):
            if n == 0 or W == 0 :
                return 0
            if (wt[n-1] > W):
                return knapSack(W, wt, val, n-1)
            else:
                return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                    knapSack(W, wt, val, n-1))
        
        if classi =="FirstClass":
            W=40
        elif classi == "Bussiness":
            W=35
        elif classi == "Economy":
            W=25
        else:
            W=10
        n = len(val)
        print (knapSack(W, wt, val, n))
        w=knapSack(W, wt, val, n)
        return render(request, 'weight.html',{'Knap':w,'Total':total})
    return render(request, 'weight.html')