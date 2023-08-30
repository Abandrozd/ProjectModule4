from django.urls import path
from .views import index, top_sellers, advert_post, advert_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advert_post, name='adv-post'),
    path('advertsiement/<int:pk>', advert_detail, name='adv-detail')
]