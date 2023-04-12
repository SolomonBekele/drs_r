from django.urls import path
from .views import *
urlpatterns = [
    
    path("",recommend,name='recommend'),
]