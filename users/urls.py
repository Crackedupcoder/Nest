from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login-user'),
    path('user/<str:pk>/', views.about, name='about'),
    path('setting/', views.setting, name='setting'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('password-change/', views.changePassword, name='password-change'),

]