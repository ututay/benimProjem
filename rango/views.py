from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Merhaba Dünya! Bu bir rango uygulamasıdır!")