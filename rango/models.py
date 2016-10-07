from django.db import models
class Kategori(models.Model):
    kategoriIsim = models.CharField(max_length=128,unique=True)
    class Meta:
        verbose_name_plural="Kategoriler"
    def __str__(self):
        return self.kategoriIsim
class Sayfa(models.Model):
    iliski = models.ForeignKey(Kategori)
    sayfaIsim = models.CharField(max_length=128)
    sayfaUrl = models.URLField()
    sayfaGoruntuleme = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural="Sayfalar"
    def __str__(self):
        return self.sayfaIsim