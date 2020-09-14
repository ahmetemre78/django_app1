from django.shortcuts import render,redirect
from .forms import KayitOl,GirisYap

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from django.contrib import messages

# Create your views here.
def kayitol(request):
    form = KayitOl(request.POST or None)
    if form.is_valid():
      kullaniciadi = form.cleaned_data.get("k_adi")
      sifre = form.cleaned_data.get("k_sifre")

      yenikullanici = User(username = kullaniciadi)
      yenikullanici.set_password(sifre)
      yenikullanici.save()

      login(request,yenikullanici)
      messages.success(request,"Başarıyla Kayıt Oldunuz")

      return redirect("home")
    form_icerik = {
        "form" : form,
     }
    return render(request,"register.html",form_icerik)
def girisyap(request):
    form = GirisYap(request.POST or None)
    form_icerik = {
        "form":form
    }
    if form.is_valid():
        kullaniciadi = form.cleaned_data.get("kullaniciadi")
        sifre = form.cleaned_data.get("sifre")
        kullanici = authenticate(username = kullaniciadi,password = sifre)   
        if kullanici is None:
            messages.warning(request,"Kullanıcı Adı veya Şifre Hatalı")
            return render(request,"login.html",form_icerik)
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,kullanici)
        return redirect("home")
    return render(request,"login.html",form_icerik)
def cikisyap(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yapıldı...")
    return render(request,"index.html")
