from django.shortcuts import render, redirect
from .models import Laptop
from .forms import LaptopForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_url')
def lapForm(request):
    form = LaptopForm()
    template_name = 'LaptopApp/laptopform.html'
    context={'form':form}
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        e=request.POST
        print(e)
        if form.is_valid():
            form.save()
            return redirect('lap_table')
    return render(request, template_name, context)

@login_required(login_url='login_url')
def LapView(request):
    obj = Laptop.objects.all()
    template_name = 'LaptopApp/laptoptable.html'
    context= {'obj':obj}
    return render(request, template_name, context)

def updateLap(request,id):
    obj = Laptop.objects.get(laptop_id=id)
    form = LaptopForm(instance=obj)
    template_name = 'LaptopApp/laptopform.html'
    context={'form':form}
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('lap_table')
    return render(request, template_name, context)

def deleteLap(request, id):
    obj = Laptop.objects.get(laptop_id=id)
    template_name= 'LaptopApp/confirm.html'
    context = {"obj":obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('lap_table')
    return render(request, template_name, context)



# Create your views here.
