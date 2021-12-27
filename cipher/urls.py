from django.urls import path
from . import views

app_name='cipher'
urlpatterns = [
    path('', views.cipher, name='cipher'),
    path('result/', views.result, name='result')
]