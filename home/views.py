from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.forms import EmailForm


def landing(request):
    return render(request, 'landing.html')


def bootstrap(request):
    return render(request, 'bootstrap_template.html')

def email_input(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success, Thank You!")
        else:
            form = EmailForm()
        return render(request,'landing.html', {'form': form})