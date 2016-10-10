from django.contrib import admin
from rango.models import Kategori,Sayfa
class SayfaAdmin(admin.ModelAdmin):
    list_display = ("sayfaIsimDef","kategoriDef","sayfaUrlDef")
class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields = {"harfDizisi":("kategoriIsim",)}
admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Sayfa,SayfaAdmin)