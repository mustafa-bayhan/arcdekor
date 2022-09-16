from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
Kategoriler =(("Galeri","Galeri"),
              ("Mutfak","Mutfak"),
              ("Salon","Salon"),
              ("Banyo", "Banyo"),
              ("Koridor", "Koridor"),
              ("Ofis", "Ofis"))
class Contact (models.Model):
    isim=models.CharField(null=True, max_length=200)
    mail=models.CharField(null=True, max_length=200)
    telefon=models.CharField(null=True, max_length=200)
    mesaj=RichTextField()

    def __str__(self):
        return self.isim
    
    

class Gallery (models.Model):
    resim = models.ImageField(null=True, upload_to='image/')
    kategori = models.CharField(null=True, choices=Kategoriler, max_length=50)
    def __str__(self):
        return self.kategori
    
    
class Home_image (models.Model):
    name_1 = models.CharField(null=True, max_length=100)
    resim1 = models.ImageField(null=True, upload_to='image/')
    name_2 = models.CharField(null=True, max_length=100)
    resim2 = models.ImageField(null=True, upload_to='image/')
    name_3 = models.CharField(null=True, max_length=100)
    resim3 = models.ImageField(null=True, upload_to='image/')
    name_4 = models.CharField(null=True, max_length=100)
    resim4 = models.ImageField(null=True, upload_to='image/')
    name_5 = models.CharField(null=True, max_length=100)
    resim5 = models.ImageField(null=True, upload_to='image/')
    name_6 = models.CharField(null=True, max_length=100)
    resim6 = models.ImageField(null=True, upload_to='image/')
    name_7 = models.CharField(null=True, max_length=100)
    resim7 = models.ImageField(null=True, upload_to='image/')
    name_8 = models.CharField(null=True, max_length=100)
    resim8 = models.ImageField(null=True, upload_to='image/')
    def __str__(self):
        return "8 resim"
    

       
    
    
    
    
    
    
    
    
    
    
    
    
    