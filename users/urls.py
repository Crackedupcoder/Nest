from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('about/<str:pk>/', views.about, name='about'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('setting/', views.setting, name='setting'),

]