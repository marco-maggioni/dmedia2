from django.shortcuts import HttpResponse, render

# Create your views here.

def homepage(request):
    return HttpResponse('<h3>funziona</h3>')