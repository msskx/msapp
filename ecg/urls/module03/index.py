from django.urls import path

from ecg.views.module03.index import heart_classification

urlpatterns = [
    path("", heart_classification, name="heart_classification")
]
