from django.shortcuts import render

def home(request):
    return render(request, "flatpages/static_handler.html")