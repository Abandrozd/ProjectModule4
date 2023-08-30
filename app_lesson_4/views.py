from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Advert
from .forms import Advert_Model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

def index(request):
    title = request.GET.get('query')
    if title:
        adverts = Advert.objects.filter(title__irregex=title)
    else:
        adverts = Advert.objects.all()
    context = {'adverts': adverts, 'title': title}
    return render(request, 'app_lesson_4/index.html', context)


def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')

    context = {'users': users}

    return render(request, 'app_lesson_4/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advert_post(request):
    if request.method == "POST":
        form = Advert_Model(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = Advert_Model()
    context = {'form': form}
    return render(request, 'app_lesson_4/advertisement-post.html', context)

def advert_detail(request, pk):

    advert = Advert.objects.get(id=pk)
    context = {'advert': advert}
    return render(request, 'app_lesson_4/advertisement-post.html')