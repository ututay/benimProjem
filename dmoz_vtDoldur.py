import re,sys,random
from urllib.request import urlopen
from veritabani_doldur import VeritabanıDoldur
class Dmoz():
    kategoriBul = re.compile("""<TITLE>(.+)</TITLE>""")
    siteAdresiBul = re.compile("""<a target="_blank" href="(.+)">""")
    siteAdıBul = re.compile("""<div class="site-title">(.+) </div>""")
    def __init__(self,adres):
        self.site = urlopen(adres)
        self.liste = list()
        self.kategori = str()  # Veritabanına eklenecek kategori adı
        self.siteAdı = list()  # Veritabanına eklenecek site adı
        self.siteAdresi = list()  # Veritabanına eklenecek site adresi
        self.adresBulundu = False
        self.adBulundu = False
        self.main()
    def main(self):
        for veri in self.site:
            veri = veri.decode("utf-8")
            if not veri.isspace():
                veri=veri.lstrip()
                self.liste.append(veri)

        # BAŞLANGIÇ-Kategori bulan kodlar.
        for veri in self.liste:
            nesne = re.search(self.kategoriBul,veri)
            if nesne:
                self.kategori = nesne.group(1).split(": ")[-1]
                break
        # BİTİŞ-Kategori bulan kodlar.

        # BAŞLANGIÇ-Sitelerin adı ve adresini bulan kodlar.
        for veri in self.liste:
            if veri.startswith("""<div class="title-and-desc">"""):
                self.adresBulundu=True
                continue
            if self.adresBulundu:
                nesne = re.search(self.siteAdresiBul,veri)
                if nesne:
                    self.siteAdresi.append(nesne.group(1))
                    self.adresBulundu=False
                    self.adBulundu=True
                    continue
            if self.adBulundu:
                nesne = re.search(self.siteAdıBul, veri)
                if nesne:
                    self.siteAdı.append(nesne.group(1))
                    self.adBulundu=False
        # BİTİŞ-Sitelerin adı ve adresini bulan kodlar.

if __name__ == '__main__':
    argüman = len(sys.argv)
    if argüman < 2 or argüman >= 3:
        print("Lütfen geçerli argüman giriniz!")
        exit()
    nesne = Dmoz(sys.argv[1])
    vtDoldur = VeritabanıDoldur()
    kategori = vtDoldur.kategori_ekle(nesne.kategori, beğeni=random.randint(0, 300),görüntüleme=random.randint(0, 300))
    siteler = dict(zip(nesne.siteAdı,nesne.siteAdresi))
    for isim,adres in siteler.items():
        vtDoldur.sayfa_ekle(kategori,isim,adres)