from django.shortcuts import render
from .forms import airports

def index(request):
    form = airports()
    return render(request, 'index.html', {"form":form})

