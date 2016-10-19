from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
# Kategori model 'i içeri aktrılıyor.
from rango.models import Kategori,Sayfa
# Kategori form 'u içeri aktarılıyor.ü
from rango.formlar import KategoriForm,SayfaForm

def anasayfa(request):
    kategoriler = Kategori.objects.order_by("-kategoriBegeni")[:5]
    sayfalar = Sayfa.objects.order_by("-sayfaGoruntuleme")[:5]
    içerik = {
        "kategoriler":kategoriler,
        "sayfalar":sayfalar,
    }
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

def kategoriEkle(request):
    formBilgisi = KategoriForm()
    if request.method == "POST":
        formBilgisi = KategoriForm(request.POST)
        if formBilgisi.is_valid():
            kategori = formBilgisi.save(commit=True)
            print(kategori,kategori.slug)
            return anasayfa(request)
        else:
            print(formBilgisi.errors)
    içerik = {"bilgiler":formBilgisi}
    return render(request, "rango/kategori-ekle.html", context=içerik)

def sayfaEkle(request,kategoriAdresi):
    try:
        kategori = Kategori.objects.get(slug=kategoriAdresi)
    except Kategori.DoesNotExist:
        kategori = None
    formBilgi = SayfaForm()
    if request.method == "POST":
        formBilgi = SayfaForm(request.POST)
        if formBilgi.is_valid():
            if kategori:
                sayfa = formBilgi.save(commit=False)
                sayfa.kategori=kategori
                sayfa.save()
                print(sayfa,sayfa.sayfaUrl)
                return HttpResponseRedirect(
                    reverse(
                        "rango:sayfalarıGöster",
                        kwargs={"kategoriAdresi":kategoriAdresi},
                    )
                )
        else:
            print(formBilgi.errors)
    içerik = {"formBilgi":formBilgi,"kategori":kategori}
    return render(request,"rango/sayfa-ekle.html",context=içerik)






























