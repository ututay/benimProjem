from django.conf.urls import url
from rango import views

app_name = "rango"
urlpatterns = [
    url(r"^$",views.index,name="anasayfa"),
    url(r"^about/",views.about,name="hakkımda"),
    url(r"^kategori/(?P<kategoriAdresi>[\w\-]+)/$",views.sayfalarıGöster,name="sayfalarıGöster"),
]