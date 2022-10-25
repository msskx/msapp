from django.shortcuts import render


def index(request):
    # return render(request, "multiends/main/elements.html")
    return render(request, "multiends/main/index.html")
