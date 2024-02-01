from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<slug:tag_slug>/', views.index, name='index-by-tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post, name='post'),
    path('scholarship/', views.scholarship, name='scholarship'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.teamAbout, name='about-team'),
    path('post/<str:pk>/comment/', views.post_comment, name='post-comment'),
    
]