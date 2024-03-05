from django.urls import path
from .import views

urlpatterns =[
    path('', views.coffee, name='Coffee'),
    path('home/',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('about_us/',views.about_us, name='about_us'),
    path('chocolate/',views.chocolate, name='chocolate')
]
