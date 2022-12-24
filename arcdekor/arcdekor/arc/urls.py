from django.urls import path
from . import views
urlpatterns=[ 
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('about-us',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('contact-us',views.contact,name='contact-us'),
]