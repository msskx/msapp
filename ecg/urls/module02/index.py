from django.urls import path
from ecg.views.module02.index import heart_disease

urlpatterns = [
    path("", heart_disease, name="heart_disease")
]
