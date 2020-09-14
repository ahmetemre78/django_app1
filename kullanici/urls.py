from django.contrib import admin
from django.urls import path

from . import views

app_name = "kullanici"

urlpatterns = [
    path('kayitol/', views.kayitol,name = "kayitol"),
    path('girisyap/', views.girisyap,name = "girisyap"),
    path('cikisyap/', views.cikisyap,name = "cikisyap"),
    
]