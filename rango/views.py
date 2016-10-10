from django.shortcuts import render
# Kategori model 'i içer aktrılıyor.
from rango.models import Kategori

def index(request):
    kategoriler = Kategori.objects.order_by("-kategoriBegeni")[:5]
    içerik = {"kategoriler":kategoriler}
    return render(request,"rango/index.html",context=içerik)
def about(request):
    şablonDeğişkenleri = {"isimsoyisim":"Ünal TUTAY"}
    return render(request,"rango/about.html",context=şablonDeğişkenleri)