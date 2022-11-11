from django.shortcuts import render
from .forms import  AptForm
from .models import airportModel


def index(request):
    form = AptForm()

    if request.method == 'POST':
        #Have only 1 object at a time, delete all previous
        airportModel.objects.all().delete()
        #print(request.POST)
        form = AptForm(request.POST)
        if form.is_valid():
            form.save()
        startApt = request.POST.getlist('startApt')
        endApt = request.POST.getlist('endApt')
        print(startApt)
        print(endApt)
    context = {'form':form}
    return render(request, 'index.html', context)

