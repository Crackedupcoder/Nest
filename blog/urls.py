from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<slug:tag_slug>/', views.index, name='index-by-tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('post-new/', views.createPost, name='post-new'),
    path('post/<str:pk>/update/', views.updatePost, name='post-update'),
    path('post/<str:pk>/comment/', views.post_comment, name='post-comment'),
    
]