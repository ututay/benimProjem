from django import forms
from rango.models import Kategori, Sayfa


class KategoriForm(forms.ModelForm):
    kategoriIsim = forms.CharField(
                                   max_length=128,
                                   help_text="Bir kategori ismi belirleyiniz:"
                                   )
    kategoriGoruntuleme = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    kategoriBegeni      = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug                = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model  = Kategori
        fields = ("kategoriIsim",)


class SayfaForm(forms.ModelForm):
    sayfaIsim        = forms.CharField(
                                       max_length = 128,
                                       help_text  = "Eklencek sayfa ismini giriniz:"
                                       )
    sayfaGoruntuleme = forms.IntegerField(
                                          widget  = forms.HiddenInput(),
                                          initial = 0
                                          )
    sayfaUrl         = forms.URLField(
                                      max_length = 200,
                                      help_text  = "Sayfa adresini giriniz:"
                                      )

    def clean(self):
        temizVeri = self.cleaned_data
        adres     = temizVeri["sayfaUrl"]
        if adres and not adres.startswith("http://"):
            adres = "http://" + adres
        temizVeri["sayfaUrl"] = adres
        return temizVeri

    class Meta:
        model   = Sayfa
        exclude = ("kategori",)
