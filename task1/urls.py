from django.urls import path
from .views import *

urlpatterns = [
    path('catalog', catalog, name='task1_catalog'),
    path('cart', cart, name='task1_cart'),
    path('sign_up_html', sign_up_by_html, name='task1_sign_up_by_html'),
    path('sign_up_django', sign_up_by_django, name='task1_sign_up_by_django'),
    path('news', news, name='task1_news'),
]
