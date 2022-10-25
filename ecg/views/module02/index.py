from django.shortcuts import render


def heart_disease(request):
    return render(request, "multiends/module02/heartDisease.html")
