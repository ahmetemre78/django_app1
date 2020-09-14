from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import MakaleEkle
from .models import Makale,MakaleYorum
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    """return HttpResponse("<h3>Sitemize Hoşgeldiniz</h3>")""" #-> HttpResponse ile böyle çektik
    return render(request,"index.html") #render ile de direk dosyayı template olarak çekebiliyoruz

def about(request):
    return render(request,"about.html")

def detail(request,id):
    return HttpResponse("Makale No : " + str(id))

@login_required(login_url="kullanici:girisyap")
def dashboard(request):
    articles = Makale.objects.filter(yazar_id = request.user)
    context = {
        "articles":articles
        }
    return render(request,"dashboard.html",context)

@login_required(login_url="kullanici:girisyap")
def makaleekle(request):
    form = MakaleEkle(request.POST or None,request.FILES or None)
    if form.is_valid():
        makale = form.save(commit=False)
        makale.yazar = request.user
        makale.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("home")

    return render(request,"addarticle.html",{"form":form})

def makaledetay(request,id):
    #makale = Makale.objects.filter(id = id).first()
    makale = get_object_or_404(Makale,id = id)
    yapilanyorumlar = makale.yorumlar.all()
    return render(request,"detail.html",{"article":makale,"comments":yapilanyorumlar})

@login_required(login_url="kullanici:girisyap")
def makaleguncelle(request,id):
    makale = get_object_or_404(Makale,id = id)
    form = MakaleEkle(request.POST or None, request.FILES or None, instance = makale)
    if form.is_valid():
        makale = form.save(commit=False)
        makale.yazar = request.user
        makale.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("makale:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url="kullanici:girisyap")
def makalesil(request,id):
    makale = get_object_or_404(Makale,id = id)
    makale.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("makale:dashboard")

def makaleler(request):
    arama = request.GET.get("search")
    if arama:
        articles = Makale.objects.filter(baslik__contains = arama)
        return render(request,"articles.html",{"articles":articles})

    makaleler = Makale.objects.all()
    return render(request,"articles.html",{"articles":makaleler,})

def yorumekle(request,id):
    makale = get_object_or_404(Makale,id = id)
    if request.method == "POST":
        yorum_yazar = request.POST.get("yorum_yazar")
        yorum_icerik = request.POST.get("yorum_icerik")

        yeniyorum = MakaleYorum(yorum_yazar = yorum_yazar,yorum_icerik = yorum_icerik)
        yeniyorum.makale = makale
        yeniyorum.save()
    return redirect(reverse("makale:detail",kwargs={"id":id}))