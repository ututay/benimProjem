# View 'lar içinde response vermek için çeşitli yardımcı metaryaller içe aktarılıyor.
# Başlangıç
from django.shortcuts import (
                              render,
                              reverse
                              )
from django.http import (
                         HttpResponseRedirect,
                         )
# Bitiş

# Kategori ve Sayfa modeli içeri akratılıyor.
from rango.models import (
                          Kategori,
                          Sayfa
                          )
# Form verileri içeri aktarılıyor.
from rango.formlar import (
                           KategoriForm,
                           SayfaForm,
                           KullaniciForm,
                           KullaniciBilgisiForm
                           )
# İşlem yapabilmek için sisteme login olunması gereken View 'lar için
# login_required bezeyicisi sisteme eklendi.
from django.contrib.auth.decorators import login_required
# Zaman bilgisini Cookie 'ler der kullanabilmek içni datetime kütüphanesi içe aktarılıyor.
from datetime import datetime


def anasayfa(request):
    ziyaretSayaci(request)
    kategoriler = Kategori.objects.order_by("-kategoriBegeni")[:5]
    sayfalar    = Sayfa.objects.order_by("-sayfaGoruntuleme")[:5]
    içerik      = {
        "kategoriler": kategoriler,
        "sayfalar"   : sayfalar,
    }
    cevap = render(request, "rango/index.html", context=içerik)
    return cevap


def about(request):
    ziyaretSayaci(request)
    şablonDeğişkenleri = {"isimsoyisim": "Ünal TUTAY"}
    return render(request, "rango/about.html", context=şablonDeğişkenleri)


def sayfalarıGöster(request, kategoriAdresi):
    ziyaretSayaci(request)
    içerik = dict()
    try:
        kategori           = Kategori.objects.get(slug=kategoriAdresi)
        sayfalar           = Sayfa.objects.filter(kategori=kategori)
        içerik["kategori"] = kategori
        içerik["sayfalar"] = sayfalar
    except Kategori.DoesNotExist:
        içerik["kategori"] = None
        içerik["sayfalar"] = None
        print("{} adresiyle eşleşen herhangi bir kategori bulunamadı.".format(
            kategoriAdresi))
    return render(request, "rango/kategoriler.html", context=içerik)


@login_required
def kategoriEkle(request):
    ziyaretSayaci(request)
    formBilgisi = KategoriForm()
    if request.method == "POST":
        formBilgisi = KategoriForm(request.POST)
        if formBilgisi.is_valid():
            formBilgisi.save(commit=True)
            return anasayfa(request)
        else:
            print("Hata yazdırılıyor:", formBilgisi.errors)
    içerik = {"bilgiler": formBilgisi}
    return render(request, "rango/kategori-ekle.html", context=içerik)


@login_required
def sayfaEkle(request, kategoriAdresi):
    ziyaretSayaci(request)
    try:
        kategori = Kategori.objects.get(slug=kategoriAdresi)
    except Kategori.DoesNotExist:
        kategori = None
    formBilgi = SayfaForm()
    if request.method == "POST":
        formBilgi = SayfaForm(request.POST)
        if formBilgi.is_valid():
            if kategori:
                sayfa          = formBilgi.save(commit=False)
                sayfa.kategori = kategori
                sayfa.save()
                return HttpResponseRedirect(
                    reverse(
                        "rango:sayfalarıGöster",
                        kwargs={"kategoriAdresi": kategoriAdresi},
                    )
                )
        else:
            print(formBilgi.errors)
    içerik = {"formBilgi": formBilgi, "kategori": kategori}
    return render(request, "rango/sayfa-ekle.html", context=içerik)


def ziyaretSayaci(request):
    ziyaretSayisiCookie = int(request.session.get("ziyaretSayisi", "1"))
    sonZiyaretCookie    = request.session.get("sonZiyaret", str(datetime.today()))
    sonZiyaretNesne     = datetime.strptime(sonZiyaretCookie[:-7], "%Y-%m-%d %H:%M:%S")
    if (datetime.now() - sonZiyaretNesne).seconds > 0:
        ziyaretSayisiCookie += 1
        request.session["sonZiyaret"] = str(datetime.today())
    else:
        request.session["sonZiyaret"] = sonZiyaretCookie
    request.session["ziyaretSayisi"] = ziyaretSayisiCookie
    return ziyaretSayisiCookie


def kayit(request):
    print("İSTEK YAPILDI", request)
    hata = dict()
    kullanici = KullaniciForm()
    profil = KullaniciBilgisiForm()
    if request.method == "POST":
        kullanici = KullaniciForm(request.POST)
        profil = KullaniciBilgisiForm(request.POST)
        if kullanici.is_valid() and profil.is_valid():
            kullanici = kullanici.save(commit=True)
            profil = profil.save(commit=False)
            if "profilResim" in request.FILES:
                profil.profilResim = request.FILES["profilResim"]
            profil.kullanici = kullanici
            profil.save()
            return HttpResponseRedirect(reverse("registration_complete"))
        else:
            if not kullanici.is_valid():
                hata.update(kullanici.errors)
                print(kullanici.errors)
            if not profil.is_valid():
                hata.update(profil.errors)
                print(profil.errors)
    print(hata)
    içerik = {
            "kullanici": kullanici,
            "profil": profil,
            "hata": hata
    }
    return render(request, "registration/registration_form.html", içerik)
