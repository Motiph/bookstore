from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorModelViewSet, BookModelViewSet


router = DefaultRouter()
router.register(r'authors', AuthorModelViewSet, basename='authors')
router.register(r'books', BookModelViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls))
]