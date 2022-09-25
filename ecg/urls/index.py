from django.urls import path, include
from ecg.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("main/", include("ecg.urls.main.index"))
    # path("", index, name="index")
    # path("", index, name="index")
]
