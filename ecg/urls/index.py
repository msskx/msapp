from django.urls import path, include

urlpatterns = [
    # path("", index, name="index"),
    path("main/", include("ecg.urls.main.index")),
    path("module01/", include("ecg.urls.module01.index"))
    # path("", index, name="index")
    # path("", index, name="index")
]
