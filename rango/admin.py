from django.contrib import admin
from rango.models import Kategori,Sayfa
class SayfaInline(admin.StackedInline):
    model = Sayfa
    extra = 3
class SayfaAdmin(admin.ModelAdmin):
    list_display = ("sayfaIsimDef","kategoriDef","sayfaUrlDef")
admin.site.register(Kategori)
admin.site.register(Sayfa,SayfaAdmin)