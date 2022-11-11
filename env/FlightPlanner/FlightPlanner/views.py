from django.shortcuts import render
from .forms import  AptForm
from .models import airportModel
import pandas as pd


def index(request):
    form = AptForm()

    if request.method == 'POST':
        #Have only 1 object at a time, delete all previous
        airportModel.objects.all().delete()
        #print(request.POST)
        form = AptForm(request.POST)
        if form.is_valid():
            form.save()
        #Get the start and ending airports
        startApt = request.POST.getlist('startApt')
        endApt = request.POST.getlist('endApt')
        #Get rid of the brackets and single quotes around to pass them into function
        cleanStartApt = ''.join(startApt)
        cleanEndApt = ''.join(endApt)
        #print as a test
        #print(cleanStartApt)
        #print(cleanEndApt)
    context = {'form':form, 'startApt':cleanStartApt, 'endApt':cleanEndApt}
    return render(request, 'index.html', context)

