from django import forms
from .models import Makale
class MakaleEkle(forms.ModelForm):
    class Meta:
        model = Makale
        fields = ["baslik","icerik","resim"]