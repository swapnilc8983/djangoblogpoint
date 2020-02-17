
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    # path('contact/', views.Contactform, name="contactform"),
    path('<slug:slug>/', views.blog, name="blog"),
   
]