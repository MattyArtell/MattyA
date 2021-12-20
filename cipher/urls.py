from django.urls import path
from . import views

app_name='cipher'
urlpatterns = [
    path('', views.home, name='home'),
    path('cipher/', views.cipher, name='cipher'),
]