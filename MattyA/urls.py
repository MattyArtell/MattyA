from django.contrib import admin
from django.urls import path
from cipher import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cipher/', views.cipher, name='cipher'),
]