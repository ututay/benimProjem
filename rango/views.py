from django.shortcuts import render
# Kategori model 'i içer aktrılıyor.
from rango.models import Kategori,Sayfa

def index(request):
    kategoriler = Kategori.objects.order_by("-kategoriBegeni")[:5]
    içerik = {"kategoriler":kategoriler}
    return render(request,"rango/index.html",context=içerik)

def about(request):
    şablonDeğişkenleri = {"isimsoyisim":"Ünal TUTAY"}
    return render(request,"rango/about.html",context=şablonDeğişkenleri)

def sayfalarıGöster(request,kategoriAdresi):
    içerik = dict()
    try:
        kategori = Kategori.objects.get(slug=kategoriAdresi)
        sayfalar = Sayfa.objects.filter(kategori=kategori)
        içerik["kategori"]=kategori
        içerik["sayfalar"]=sayfalar
    except Kategori.DoesNotExist:
        içerik["kategori"]=None
        içerik["sayfalar"]=None
        print("{} adresiyle eşleşen herhangi bir kategori bulunamadı.".format(kategoriAdresi))
    return render(request,"rango/kategoriler.html",context=içerik)