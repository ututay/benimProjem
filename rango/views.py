# View 'lar içinde response vermek için çeşitli yardımcı metaryaller içe aktarılıyor.
# Başlangıç
from django.shortcuts import (
                              render,
                              reverse
                              )
from django.http import (
                         HttpResponseRedirect,
                         HttpResponse
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
                           KullaniciBilgisiForm,
                           KullaniciForm
                           )
# Sisteme kullanıcı girişini sağlamak için gerekli metaryaller içe aktarılıyor.
from django.contrib.auth import (
                                 authenticate,
                                 login,
                                 logout,
                                 )
# İşlem yapabilmek için sisteme login olunması gereken View 'lar için
# login_required bezeyicisi sisteme eklendi.
from django.contrib.auth.decorators import login_required


def anasayfa(request):
    kategoriler = Kategori.objects.order_by("-kategoriBegeni")[:5]
    sayfalar    = Sayfa.objects.order_by("-sayfaGoruntuleme")[:5]
    içerik      = {
        "kategoriler": kategoriler,
        "sayfalar"   : sayfalar,
    }
    return render(request, "rango/index.html", context=içerik)


def about(request):
    şablonDeğişkenleri = {"isimsoyisim": "Ünal TUTAY"}
    return render(request, "rango/about.html", context=şablonDeğişkenleri)


def sayfalarıGöster(request, kategoriAdresi):
    print("Login Durumu -->", request.user.is_authenticated())
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


def kullaniciKayit(request):
    kayit = False
    formBilgi_kullanici = KullaniciForm()
    formBilgi_profil    = KullaniciBilgisiForm()
    hatalar = str()
    if request.method == "POST":
        formBilgi_kullanici = KullaniciForm(request.POST)
        formBilgi_profil    = KullaniciBilgisiForm(request.POST)
        if formBilgi_kullanici.is_valid() and formBilgi_profil.is_valid():
            kullanici = formBilgi_kullanici.save()
            kullanici.set_password(kullanici.password)
            kullanici.save()
            profil           = formBilgi_profil.save(commit=False)
            profil.kullanici = kullanici
            if "profilResim" in request.FILES:
                profil.profilResim = request.FILES["profilResim"]
            print("Profil Resmi", request.FILES)
            profil.save()
            kayit = True
        else:
            hatalar = str(formBilgi_profil.errors) + str(formBilgi_kullanici.errors)
    içerikler = {
                "kullanici" : formBilgi_kullanici,
                "profil"    : formBilgi_profil,
                "kayit"     : kayit,
                "hatalar"   : hatalar
                }
    return render(request, "rango/kullanici-kayit.html", context=içerikler)


def giris(request):
    if request.method == "POST":
        kullanici_adi = request.POST.get("kullanici_adi")
        sifre         = request.POST.get("sifre")
        kullanici     = authenticate(username=kullanici_adi, password=sifre)
        if kullanici:
            if kullanici.is_active:
                login(request, kullanici)
                return HttpResponseRedirect(reverse("rango:anasayfa"))
            else:
                print("{0} kullanıcı adı ve {1} şifreli hesap aktif değil!".format(kullanici_adi, sifre))
        else:
            return HttpResponse("Yanlış kullanıcı adı veya şifre girdiniz.")
    return render(request, "rango/giris.html")


@login_required
def cikisYap(request):
    logout(request)
    return HttpResponseRedirect(reverse("rango:anasayfa"))
