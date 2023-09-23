from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about, name="about"),
    path('visit/', views.visit, name="visit"),
    path('contact/', views.contact, name="contact"),
    # path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="sample"),
]
