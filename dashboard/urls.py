from django.urls import path
from . import views

# app_name = 'dashboard'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('password/', views.password, name = 'password'),
    path('logout/', views.logout, name = 'logout'),
]
