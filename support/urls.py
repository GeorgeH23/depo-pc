from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact'),
    path('t_and_c/', views.t_and_c, name='t_and_c'),
    path('privacy/', views.privacy, name='privacy'),
]
