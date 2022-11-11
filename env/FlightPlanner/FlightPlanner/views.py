from django.shortcuts import render
from .forms import  startAptForm

def index(request):
    form = startAptForm()

    if request.method == 'POST':
        print(request.POST)
        form = startAptForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'index.html', context)

