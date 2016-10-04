from django.db import models
class Kategori(models.Model):
    kategoriIsim = models.CharField(max_length=128,unique=True)
    def str(self):
        return self.name
class Sayfa(models.Model):
    iliski = models.ForeignKey(Kategori)
    sayfaIsim = models.CharField(max_length=128)
    sayfaUrl = models.URLField()
    sayfaGoruntuleme = models.IntegerField(default=0)
    def str(self):
        return self.name