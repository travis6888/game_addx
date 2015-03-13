from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def bootstrap(request):
    return render(request, 'bootstrap_template.html')
