from django.urls import path
from .views import *
urlpatterns = [
    path("",re_home,name="re_home"),
    path("interview",interview,name="interview"),
    path("recommend",recommend,name='recommend'),
]