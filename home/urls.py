from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('contactform/', views.contactform, name='contactform'),
    path('bookingtable/', views.bookingtable, name='bookingtable'),
    path('meal/', views.meal, name='meal'),
    path('bookmeal/', views.bookmeal, name='bookmeal'),
    path('datasend/', views.datasend, name='datasend'),
    path('datasendmeal/', views.datasendmeal, name='datasendmeal'),
    
]
