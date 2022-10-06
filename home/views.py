from django.shortcuts import render
from django.http import HttpResponse
from . models import ContactForm, BookingTable, BookMeal
# Create your views here.
def index(request):
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def booking(request):
    return render(request,'booking.html')

def meal(request):
    return render(request,'meal.html')

def datasend(request):
    return render(request,'datasend.html')

def datasendmeal(request):
    return render(request,'datasendmeal.html')

def contactform(request):
    if request.method == "POST":
        finam = request.POST.get("f_firstname")
        anam = request.POST.get("f_lastname")
        em = request.POST.get("f_email")
        sub = request.POST.get("f_subject")
        mes = request.POST.get("f_message")
        abc = ContactForm(firstname=finam, lastname=anam, email=em, subject=sub, message=mes)
        abc.save()
        return render(request, 'datasend.html')
    else:
        return render(request, 'index.html')

def bookingtable(request):
    if request.method == "POST":
        fim = request.POST.get("b_firstname")
        lam = request.POST.get("b_lastname")
        ema = request.POST.get("b_email")
        tat = request.POST.get("b_tabletype")
        gnum = request.POST.get("b_guestnumber")
        pla = request.POST.get("b_placement")
        dat = request.POST.get("b_date")
        tim = request.POST.get("b_time")
        no = request.POST.get("b_note")
        xyz = BookingTable(firstname=fim, lastname=lam, email=ema, tabletype=tat, guestnumber=gnum, placement=pla, date=dat, time=tim, note=no)
        xyz.save()
        return render(request, 'datasend.html')
    else:
        return render(request, 'index.html')

def bookmeal(request):
    if request.method == "POST":
        mnam = request.POST.get("m_name")
        anam = request.POST.get("m_number")
        itnam = request.POST.get("m_itemname")
        qun = request.POST.get("m_quantity")
        jkm = BookMeal(name=mnam, number=anam, itemname=itnam, quantity=qun )
        jkm.save()
        return render(request, 'datasendmeal.html')
    else:
        return render(request, 'index.html')