from django.conf.urls import url
from rango import views

app_name    = "rango"
urlpatterns = [
    url(r"^$", views.anasayfa, name="anasayfa"),
    url(r"^about/", views.about, name="hakkimda"),
    url(r"^kategori/(?P<kategoriAdresi>[\w\-]+)/$", views.sayfalarıGöster, name="sayfalarıGöster"),
    url(r"^kategori-ekle/$", views.kategoriEkle, name="kategori-ekle"),
    url(r"^sayfa-ekle/(?P<kategoriAdresi>[\w\-]+)/$", views.sayfaEkle, name="sayfa-ekle"),
    url(r"^kullanici-kayit/$", views.kullaniciKayit, name="kullanici-kayit"),
    url(r"^giris/$", views.giris, name="giris"),
    url(r"^cikis-yap/$", views.cikisYap, name="cikis-yap"),
]
