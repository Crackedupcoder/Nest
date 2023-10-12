from django.urls import path
from . import views

urlpatterns = [
    path('login/writer/', views.loginWriter, name='login-writer'),
    path('login/user/', views.loginUser, name='login-user'),
    path('about/<str:pk>/', views.about, name='about'),
    path('setting/', views.setting, name='setting'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),

]