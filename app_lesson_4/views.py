from django.shortcuts import render
from django.http import HttpResponse
from .models import Advert

def index(request):
    adverts = Advert.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')
