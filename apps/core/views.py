from rest_framework.viewsets import ModelViewSet

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, BookDetailedSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailedSerializer

    def get_serializer_class(self):
        if self.action == 'create' or  self.action == 'update':
            return BookSerializer

        return self.serializer_class

