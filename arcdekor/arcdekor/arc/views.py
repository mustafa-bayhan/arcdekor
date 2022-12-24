from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def index(request):
    context3={}
    image = Home_image.objects.all()
    if not len(image) == 0:
        context3['image']=image[0]
    return render(request,'index.html',context3)

def about(request):
    
    return render(request,'about.html',{})


def gallery(request):
    context2={}
    resimler=Gallery.objects.all()
    context2["Banyo"] = resimler.filter(kategori="Banyo")
    context2["Salon"] = resimler.filter(kategori="Salon")
    context2["Mutfak"] = resimler.filter(kategori="Mutfak")
    context2["Koridor"] = resimler.filter(kategori="Koridor")
    context2["Ofis"] = resimler.filter(kategori="Ofis")
    context2["Galeri"] = resimler.filter(kategori="Galeri")
    return render(request,'gallery.html',context2)

def services(request):
    
    return render(request,'services.html',{})


def contact(request):
    import random
    context={}
    if request.method=="POST":
        
        result = int(request.POST.get('a')) + int(request.POST.get('b'))
        if result == int(request.POST.get('result')):
        
            make_comment = Contact.objects.create(isim=request.POST.get('name'),mail=request.POST.get('email'), telefon=request.POST.get('tel'), mesaj=request.POST.get('message'))
            make_comment.save()
            
        else:
            a = random.randint(1,50)
            b = random.randint(1,10)
            context['a']=a
            context['b']=b
            context['name']=request.POST.get('name')
            context['email']=request.POST.get('email')
            context['tel']=request.POST.get('tel')
            context['message']=request.POST.get('message')
            context['error'] = 'İşlem sonucu yanlış. Lütfen sonucu doğru giriniz!'
            return render(request,'contact.html',context)
        
    a = random.randint(1,50)
    b = random.randint(1,10)
    context['a']=a
    context['b']=b
    return render(request,'contact.html',context)

def handle_not_found(request, exception):
    context7={}
    query2=request.GET.get('search')
    if query2:
        return HttpResponseRedirect('/products?search={}'.format(query2))
    
    return render(request, '404.html',context7)