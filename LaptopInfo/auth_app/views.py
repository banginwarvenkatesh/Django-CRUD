from hashlib import new
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.conf import settings
from django.core.mail import send_mail
from random import randint

otp = randint(000000,999999)


def genrate_otp():
    return randint(100000,999999)


def registerView(request):
    form = UserCreationForm()
    template_name = 'auth_app/register.html'
    #context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    context = {'form':form}   
    return render(request, template_name, context)

def loginView(request):
    template_name='auth_app/login.html'
    context = {}

    if request.method == 'POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')
        global new
        user = authenticate(username=un, password=pw)
        new = user
        if user is not None:
            eml = request.POST.get('e')
            otp = genrate_otp()
            subject= "Your OTP for login to django app!"
            message = f"Hello {un}, your otp is: {otp}. Thank You!"
            eamil_from= settings.EMAIL_HOST_USER
            recipient_list = [eml,]
            send_mail(subject,message,eamil_from,recipient_list)
            return redirect('otp_url')
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login_url')


def OTPview(request):
    template_name = 'auth_app/otp.html'
    context={}
    if request.method == 'POST':
         otp1 = request.POST.get('otp')
         otp2 = int(otp1)
         print(otp, otp1)
         if otp == otp2:
            login(request, new)
            return redirect('lap_table')
    return render(request,template_name,context)
            
# Create your views here.
