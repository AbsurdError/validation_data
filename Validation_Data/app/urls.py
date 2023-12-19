from .views import *
from django.urls import path

urlpatterns = [
    path('', sing_up, name='sing_up'),
    path('sing_in/', sing_in, name='sing_in'),
    path('user/', user)
]
