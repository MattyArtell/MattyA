from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('signup/', views.signupuser, name="signupuser"),
	path('logout/', views.logoutuser, name='logoutuser'),
	path('login/', views.loginuser, name='loginuser'),    

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cipher/', include('cipher.urls')),
    path('quiz/', include('quiz.urls')),
]