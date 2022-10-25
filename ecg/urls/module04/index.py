from django.urls import path
from ecg.views.module04.index import heart_risk

urlpatterns = [
    path("", heart_risk, name="heart_risk")
]
