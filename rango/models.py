from django.db import models
from django.template.defaultfilters import slugify
class Kategori(models.Model):
    kategoriIsim = models.CharField(max_length=128,unique=True)
    kategoriGoruntuleme = models.IntegerField(default=0)
    kategoriBegeni = models.IntegerField(default=0)
    slug = models.SlugField(blank=True,unique=True)
    türkçeKarakter = "ığüşöçĞÜŞİÖÇ"
    karşıKarakter = "igusocGUSIOC"
    çeviri = str.maketrans(türkçeKarakter,karşıKarakter)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.kategoriIsim.translate(self.çeviri))
        super().save(*args,**kwargs)
    class Meta:
        verbose_name_plural="Kategoriler"
    def __str__(self):
        return self.kategoriIsim
class Sayfa(models.Model):
    kategori = models.ForeignKey(Kategori)
    sayfaIsim = models.CharField(max_length=128)
    sayfaGoruntuleme = models.IntegerField(default=0)
    sayfaUrl = models.URLField()
    def kategoriDef(self):
        return self.kategori
    def sayfaIsimDef(self):
        return self.sayfaIsim
    def sayfaUrlDef(self):
        return self.sayfaUrl
    kategoriDef.short_description="Sektör"
    sayfaIsimDef.short_description="Web Sitesi"
    sayfaUrlDef.short_description="Url Adresi"
    class Meta:
        verbose_name_plural="Sayfalar"
    def __str__(self):
        return self.sayfaIsim