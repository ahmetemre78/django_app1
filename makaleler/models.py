from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Makale(models.Model):
    yazar = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    baslik = models.CharField(max_length=50,verbose_name="Başlık")
    icerik = RichTextField(verbose_name="İçerik")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    resim = models.FileField(blank = True,null = True,verbose_name="Ek : ")
    def __str__(self):
        return self.baslik
    class Meta:
        ordering = ['-olusturulma_tarihi']

class MakaleYorum(models.Model):
    makale = models.ForeignKey(Makale, related_name='yorumlar', on_delete=models.CASCADE, verbose_name="Yorum Yapın")
    yorum_yazar = models.CharField(max_length=50,verbose_name="Adınız : ")
    yorum_icerik = models.CharField(max_length=200,verbose_name="Yorumunuz : ")
    yorum_tarihi = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.yorum_icerik
    class Meta:
        ordering = ['-yorum_tarihi']