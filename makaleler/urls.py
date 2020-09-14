from django.contrib import admin
from django.urls import path

from . import views

app_name = "makale"

urlpatterns = [
    path('kontrolpaneli/', views.dashboard,name = "dashboard"),
    path('makaleekle/', views.makaleekle,name = "addarticle"),
    path('makale/<int:id>', views.makaledetay,name = "detail"),
    path('guncelle/<int:id>', views.makaleguncelle,name = "update"),
    path('sil/<int:id>', views.makalesil,name = "delete"),
    path('', views.makaleler,name = "articles"),
    path('yorumlar/<int:id>', views.yorumekle,name = "comment"),
]