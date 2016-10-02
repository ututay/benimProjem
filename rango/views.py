from django.shortcuts import render
def index(request):
    şablonDeğişkenleri = {"boldmessage":"Gevrek,kremalı,kurabiye,şeker,kek"}
    return render(request,"rango/index.html",context=şablonDeğişkenleri)
def about(request):
    şablonDeğişkenleri = {"isimsoyisim":"Ünal TUTAY"}
    return render(request,"rango/about.html",context=şablonDeğişkenleri)