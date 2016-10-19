from django.conf.urls import url
from rango import views

app_name = "rango"
urlpatterns = [
    url(r"^$",views.anasayfa,name="anasayfa"),
    url(r"^about/",views.about,name="hakkımda"),
    url(r"^kategori/(?P<kategoriAdresi>[\w\-]+)/$",views.sayfalarıGöster,name="sayfalarıGöster"),
    url(r"^kategori-ekle/$",views.kategoriEkle,name="kategori-ekle"),
    url(r"^sayfa-ekle/(?P<kategoriAdresi>[\w\-]+)/$",views.sayfaEkle,name="sayfa-ekle"),
]