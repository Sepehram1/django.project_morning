from django.urls import path
from . import views
from .views import posts_list, add_post, about_me


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.about, name='about'),
    
    path('posts/', posts_list, name='posts_list'),
    path('add_post/', add_post, name='add_post'),
    path('aboutme/', about_me, name='about_me'),
    
    
    
   
]
