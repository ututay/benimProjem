from django.conf.urls import url
from rango import views

app_name    = "rango"
urlpatterns = [
    url(r"^$", views.anasayfa, name="anasayfa"),
    url(r"^about/", views.about, name="hakkimda"),
    url(r"^kategori/(?P<kategoriAdresi>[\w\-]+)/$", views.sayfalarıGöster, name="sayfalarıGöster"),
    url(r"^kategori-ekle/$", views.kategoriEkle, name="kategori-ekle"),
    url(r"^(?P<kategoriAdresi>[\w\-]+)/sayfa-ekle/$", views.sayfaEkle, name="sayfa-ekle"),
    url(r"^arama/$", views.arama, name="arama"),
    url(r"^git/", views.sayfaGit, name="git"),
]
