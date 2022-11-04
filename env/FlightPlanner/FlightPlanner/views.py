from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aircraft(request):
    return render(request, 'AircraftData.html')
