from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login-user'),
    path('<str:pk>/', views.about, name='about'),
    path('user/setting/', views.setting, name='setting'),
    path('user/logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('password-change/', views.changePassword, name='password-change'),

]