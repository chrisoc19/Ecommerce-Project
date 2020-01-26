from django.conf.urls import url, include
from .views import all_products, all_categories


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^category$', all_categories, name='category'),
]
