from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    şablonDeğişkenleri = {"boldmessage":"Gevrek,kremalı,kurabiye,şeker,kek"}
    return render(request,"rango/index.html",context=şablonDeğişkenleri)
def about(request):
    return HttpResponse("""Hakkımızda sayfasına hoşgeldiniz. -> <a href="/rango/" title="Anasayfa">Anasayfa</a>""")