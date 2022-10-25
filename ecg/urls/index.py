from django.urls import path, include

urlpatterns = [
    # path("", index, name="index"),
    path("main/", include("ecg.urls.main.index")),
    path("module01/", include("ecg.urls.module01.index")),
    path("module02/", include("ecg.urls.module02.index")),
    path("module03/", include("ecg.urls.module03.index")),
    path("module04/", include("ecg.urls.module04.index")),

]
