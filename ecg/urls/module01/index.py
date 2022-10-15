from django.urls import path
from ecg.views.module01 import data_vision

urlpatterns = [
    path("", data_vision, name="data_vision")
]
