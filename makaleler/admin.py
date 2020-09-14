from django.contrib import admin

from .models import Makale,MakaleYorum

admin.site.register(MakaleYorum)

# Register your models here.
@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ["baslik","yazar","olusturulma_tarihi"] #belirlediğimiz alanları gösteriyoruz...
    list_display_links = ["baslik","olusturulma_tarihi"] #belirlediğimiz alanlara makaleye gitmesi için link veriyoruz...
    search_fields = ["baslik"] #hangi alana göre arama butonu koyduğumuzu belirtiyoruz...
    list_filter = ["olusturulma_tarihi"] #filtelemek istediğimiz alanı verip filtre seçeneği ekliyoruz...
    class Meta:
        model = Makale


