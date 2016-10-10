# Bu dosya veritabanını okunaklı verilerle doldurmak için yaratılmıştır.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","benimProjem.settings")
import django
django.setup()
from rango.models import Kategori,Sayfa

class VeritabanıDoldur():
    def __init__(self,liste=None):
        self.liste = liste
    def doldur(self):
        for kategori,içerik in self.liste.items():
            k = self.kategori_ekle(kategori,içerik["beğeni"],içerik["görüntüleme"])
            for site in içerik["sayfalar"]:
                self.sayfa_ekle(k,site["title"],site["url"])
        self.vt_oku()

    def kategori_ekle(self,kategori,beğeni,görüntüleme=0):
        k = Kategori.objects.get_or_create(kategoriIsim=kategori)[0]
        k.kategoriBegeni = beğeni
        k.kategoriGoruntuleme = görüntüleme
        k.save()
        return k

    def sayfa_ekle(self,k,title,url,goruntuleme=0):
        s = Sayfa.objects.get_or_create(kategori=k,sayfaIsim=title)[0]
        s.sayfaUrl = url
        s.sayfaGoruntuleme = goruntuleme
        s.save()

    def vt_oku(self):
        kategoriler = Kategori.objects.all()
        for kategori in kategoriler:
            sayfalar = Sayfa.objects.filter(kategori=kategori)
            for sayfa in sayfalar:
                print("{0} - {1}".format(kategori.kategoriIsim,sayfa.sayfaIsim))

if __name__ == "__main__":
    haber = [
        {"title": "Sözcü Gazetesi", "url": "http://www.sozcu.com.tr"},
        {"title": "En Son Haber", "url": "http://www.ensonhaber.com"},
        {"title": "Hürriyet Gazetesi", "url": "http://www.hurriyet.com.tr"},
        {"title": "A Haber", "url": "http://www.ahaber.com.tr"},
        {"title": "Milliyet Haber", "url": "http://www.milliyet.com.tr"},
        {"title": "Habertürk", "url": "http://www.haberturk.com"},
    ]
    teknoloji = [
        {"title": "CHIP Online", "url": "http://www.chip.com.tr"},
        {"title": "ShiftDelete.Net", "url": "http://shiftdelete.net"},
        {"title": "Teknoloji ve Bilim Haberleri", "url": "http://www.veteknoloji.net"},
    ]
    yemek = [
        {"title": "Yemek Sepeti", "url": "http://www.yemeksepeti.com"},
        {"title": "Nefis Yemek Tarifleri", "url": "http://www.nefisyemektarifleri.com"},
        {"title": "Elele", "url": "http://www.elele.com.tr/yemek"},
        {"title": "Pratik Yemek Tarifleri", "url": "http://yemek.com"},
        {"title": "Mynet Yemek", "url": "http://yemek.mynet.com"},
    ]
    liste = {
        "Haber": {"sayfalar": haber, "beğeni": 64, "görüntüleme": 124},
        "Teknoloji": {"sayfalar": teknoloji, "beğeni": 32, "görüntüleme": 64},
        "Yemek": {"sayfalar": yemek, "beğeni": 16, "görüntüleme": 32},
    }
    nesne = VeritabanıDoldur(liste)
    nesne.doldur()
    nesne.vt_oku()
    print("Bitti!")