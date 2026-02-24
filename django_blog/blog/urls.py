from django.urls import path
from .views import search_posts, posts_by_tag
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns += [
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts_by_tag'),
]