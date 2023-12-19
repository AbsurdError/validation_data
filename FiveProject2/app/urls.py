from .views import *
from django.urls import path

urlpatterns = [
    path('my', index, name='home'),
    path('data', getData, name='data')
]
