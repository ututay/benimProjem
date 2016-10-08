# Bu dosya veritabanını okunaklı verilerle doldurmak için yaratılmıştır.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","benimProjem.settings")
import django
django.setup()
from rango.models import Kategori,Sayfa

def doldur():
    haber = [
        {"title":"Sözcü Gazetesi","url":"http://www.sozcu.com.tr"},
        {"title":"En Son Haber","url":"http://www.ensonhaber.com"},
        {"title":"Hürriyet Gazetesi","url":"http://www.hurriyet.com.tr"},
        {"title":"A Haber","url":"http://www.ahaber.com.tr"},
        {"title":"Milliyet Haber","url":"http://www.milliyet.com.tr"},
        {"title":"Habertürk","url":"http://www.haberturk.com"},
    ]
    teknoloji = [
        {"title":"CHIP Online","url":"http://www.chip.com.tr"},
        {"title":"ShiftDelete.Net","url":"http://shiftdelete.net"},
        {"title":"Teknoloji ve Bilim Haberleri","url":"http://www.veteknoloji.net"},
    ]
    yemek = [
        {"title":"Yemek Sepeti","url":"http://www.yemeksepeti.com"},
        {"title":"Nefis Yemek Tarifleri","url":"http://www.nefisyemektarifleri.com"},
        {"title":"Elele","url":"http://www.elele.com.tr/yemek"},
        {"title":"Pratik Yemek Tarifleri","url":"http://yemek.com"},
        {"title":"Mynet Yemek","url":"http://yemek.mynet.com"},
    ]
    liste = {
        "Haber" : {"sayfalar":haber,"beğeni":64,"görüntüleme":124},
        "Teknoloji" : {"sayfalar":teknoloji,"beğeni":32,"görüntüleme":64},
        "Yemek" : {"sayfalar":yemek,"beğeni":16,"görüntüleme":32},
    }
    for kategori,içerik in liste.items():
        k = kategori_ekle(kategori,içerik["beğeni"],içerik["görüntüleme"])
        for site in içerik["sayfalar"]:
            sayfa_ekle(k,site["title"],site["url"])
    vt_oku()

def kategori_ekle(kategori,beğeni,görüntüleme):
    k = Kategori.objects.get_or_create(kategoriIsim=kategori)[0]
    k.kategoriBegeni = beğeni
    k.kategoriGoruntuleme = görüntüleme
    k.save()
    return k

def sayfa_ekle(k,title,url,goruntuleme=0):
    s = Sayfa.objects.get_or_create(kategori=k,sayfaIsim=title)[0]
    s.sayfaUrl = url
    s.sayfaGoruntuleme = goruntuleme
    s.save()

def vt_oku():
    kategoriler = Kategori.objects.all()
    for kategori in kategoriler:
        sayfalar = Sayfa.objects.filter(kategori=kategori)
        for sayfa in sayfalar:
            print("{0} - {1}".format(kategori.kategoriIsim,sayfa.sayfaIsim))

if __name__ == "__main__":
    print("Vertabanı dolduruluyor...")
    doldur()
    print("Bitti!")