from django.shortcuts import render


def heart_classification(request):
    return render(request, "multiends/module03/heartClassification.html")
