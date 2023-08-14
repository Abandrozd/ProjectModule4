from django.contrib import admin
from django.urls import path, include
from app_lesson_4.views import index, top_sellers

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)