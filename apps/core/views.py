from rest_framework.viewsets import ModelViewSet

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

