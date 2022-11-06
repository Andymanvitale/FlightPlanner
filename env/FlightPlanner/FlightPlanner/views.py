from django.shortcuts import render
from .forms import airports

def index(request):
    context = {}
    context['form']= airports()
    return render(request, 'index.html', context)


def aircraft(request):
    return render(request, 'AircraftData.html')
