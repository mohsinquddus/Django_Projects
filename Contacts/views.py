from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from .models import Contacts
# Create your views here.
def index(request):
     return HttpResponse("Hello Contacts")

def insert(request):
    if request.method=='POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        phone = request.POST.get('pnumber')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contacts(name=name,phone=phone,
        email=email,desc=desc,date=date)
        contact.save()
        # return redirect("insert")
        return redirect("/contacts/display")
    return render(request,'contacts/insert.html')

def display(request):
    contacts = Contacts.objects.all()
    return render(request,'contacts/display.html',{'contacts':contacts})