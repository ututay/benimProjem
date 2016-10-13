from django.contrib import admin
from rango.models import Kategori,Sayfa
class SayfaAdmin(admin.ModelAdmin):
    list_display = ("sayfaIsimDef","kategoriDef","sayfaUrlDef")
    list_filter = ("kategori",)
class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("kategoriIsim",)}
admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Sayfa,SayfaAdmin)