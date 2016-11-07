from django import forms
from rango.models import Kategori, Sayfa, KullaniciBilgisi
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class KategoriForm(forms.ModelForm):
    kategoriIsim = forms.CharField(
                                   max_length=128,
                                   help_text="Bir kategori ismi belirleyiniz:"
                                   )

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


class KullaniciForm(UserCreationForm):
    password1 = forms.CharField(
                               widget    = forms.PasswordInput(),
                               label = 'Şifre',
                               help_text= "Şifre",
                               )
    password2 = forms.CharField(
                               widget    = forms.PasswordInput(),
                               label = 'Şifre Onay'
                               )
    username = forms.CharField(
                               label='Kullanıcı Adı'
                               )
    email    = forms.EmailField(
                                label='Email Adresi',
                                )
    first_name = forms.CharField(
                                 label = "Adınız"
                                 )
    last_name = forms.CharField(
                                label = "Soyadınız"
                                )

    class Meta:
        model  = User
        fields = (
                  "username",
                  "email",
                  "first_name",
                  "last_name"
                  )


class KullaniciBilgisiForm(forms.ModelForm):
    class Meta:
        model = KullaniciBilgisi
        fields = ("website", "profilResim",)
