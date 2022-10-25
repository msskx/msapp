from django.shortcuts import render


def index(request):
    return render(request, "multiends/main/elements.html")
