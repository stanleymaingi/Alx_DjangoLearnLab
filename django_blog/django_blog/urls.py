"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),        # list of all posts
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # create new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # view single post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # delete post
]