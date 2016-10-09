from django.db import models
class Kategori(models.Model):
    kategoriIsim = models.CharField(max_length=128,unique=True)
    kategoriGoruntuleme = models.IntegerField(default=0)
    kategoriBegeni = models.IntegerField(default=0)
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