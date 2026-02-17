from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token # type: ignore

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ListAPIView for /books/
    path('books/', BookList.as_view(), name='book-list'),

    # Include all CRUD routes from BookViewSet
    path('', include(router.urls)),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
