from django.urls import path
from . import views

app_name='quiz'
urlpatterns = [
    #Quiz
    path('', views.quiz, name='quiz'),
    path('create', views.create, name='create'),
    path('join', views.join, name='join'),
    path('room/<uid>/', views.currentroom, name='currentroom'),

]