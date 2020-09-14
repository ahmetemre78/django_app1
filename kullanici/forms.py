from django import forms

class KayitOl(forms.Form):
    kullaniciadi = forms.CharField(min_length = 8,label="Kullanıcı Adı")
    sifre = forms.CharField(min_length = 8,label = "Şifre",widget = forms.PasswordInput)
    sifreonay = forms.CharField(min_length = 8,label = "Şifreyi Onayla",widget = forms.PasswordInput)
    def clean(self):
        kullaniciadi = self.cleaned_data.get("kullaniciadi")
        sifre = self.cleaned_data.get("sifre")
        sifreonay = self.cleaned_data.get("sifreonay")
        if (sifre and sifreonay) and sifre != sifreonay:
            raise forms.ValidationError("Şifreler Uyuşmuyor")
        kayitlar = {
            "k_adi" : kullaniciadi,
            "k_sifre" : sifre,
        }
        return kayitlar

class GirisYap(forms.Form):
    kullaniciadi = forms.CharField(label="Kullanıcı Adı")
    sifre = forms.CharField(label = "Şifre",widget = forms.PasswordInput)
