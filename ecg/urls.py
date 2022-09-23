from django.urls import path
from ecg.views import index

urlpatterns=[
    path("",index,name="index"),
]