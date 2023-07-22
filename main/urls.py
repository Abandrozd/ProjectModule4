from django.contrib import admin
from django.urls import path
from app_lesson_4.views import index, top_sellers


urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
]
