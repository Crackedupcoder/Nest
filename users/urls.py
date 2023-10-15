from django.urls import path
from . import views

urlpatterns = [
    path('login/writer/', views.loginWriter, name='login-writer'),
    path('login/user/', views.loginUser, name='login-user'),
    path('user/<str:pk>/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('setting/', views.setting, name='setting'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),

]