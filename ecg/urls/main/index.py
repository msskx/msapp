
from django.urls import path
from ecg.views.main import index

urlpatterns = [
    path("", index, name="index"),

]
