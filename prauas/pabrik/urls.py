from django.urls import path
from pabrik.views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('index.html', main_page, name='main_page'),
]
