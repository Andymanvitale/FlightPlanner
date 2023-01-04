from django.shortcuts import render
from .forms import  AptForm
from .models import airportModel
from .getDistance import findDistance


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
    startApt = request.POST.getlist('Starting Airport')
    endApt = request.POST.getlist('endApt')
    #Get rid of the brackets and single quotes around to pass them into function
    cleanStartApt = ''.join(startApt)
    cleanEndApt = ''.join(endApt)
    context = {'form':form, 'Start Airport':cleanStartApt, 'endApt':cleanEndApt, 'distance': findDistance}
    return render(request, 'index.html', context)
    #context = {'form':form}
    #return render(request, 'index.html', context)

def CalcDistance(request):
    dis = findDistance()
    context = {'distance': dis}
    return render(request, 'index.html', context)

