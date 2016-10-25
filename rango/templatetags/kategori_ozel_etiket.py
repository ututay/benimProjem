from django import template
from rango.models import Kategori

# Şablon kayıt yapmak için Template paketine ait Library nesnesi oluşturuluyor.
register = template.Library()

@register.inclusion_tag("rango/sidebar_kategori_tag.html")
def kategori_listesi():
    return {"kategoriler":Kategori.objects.all()}