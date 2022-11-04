import json
from django.core.management.base import BaseCommand

from apps.core.models import Book, Author, Category

class Command(BaseCommand):
    help = 'Generate data for Book, Author, Category models'

    def create_or_get_author(self, first_name, last_name):

        author = Author.objects.filter(first_name=first_name, last_name=last_name).first()

        if author is not None:
            return author
        
        new_author = Author(first_name=first_name, last_name=last_name)
        new_author.save()

        return new_author

    
    def create_or_get_categories(self, name):
        category = Category.objects.filter(name=name).first()

        if category is not None:
            return category

        new_category = Category(name=name)
        new_category.save()

        return new_category
    
    def create_book(self, book_data, authors, categories):
        book = Book.objects.filter(isbn=book_data.get('isbn')).first()

        if book is not None:
            print('Book already exists')
            return
        
        new_book = Book(
            title=book_data.get('title'),
            isbn=book_data.get('isbn'),
            status=book_data.get('status'),
            page_count=book_data.get('pageCount'),
            thumbnail_url=book_data.get('thumbnailUrl', 'https://sciendo.com/product-not-found.png'),
            long_description=book_data.get('longDescription'),
            short_description=book_data.get('shortDescription')
        )
        
        new_book.save()

        print(authors)
        print(categories)

        new_book.authors.add(*authors)
        new_book.categories.add(*categories)

    def handle(self, *args, **options):
        json_file = open('data.json')
        books = json.load(json_file)
        for book in books:
            if book.get('isbn') and book.get('isbn') is not '':
                authors = []
                categories = []

                for author in book.get('authors'):
                    if len(author) > 0:
                        name = author.split(' ', 1)
                        if len(name) > 1:
                            first_name = name[0]
                            last_name = name[1]
                            author_obj = self.create_or_get_author(first_name, last_name)
                            authors.append(author_obj)
                
                for category in book.get('categories'):
                    category_obj = self.create_or_get_categories(category)
                    categories.append(category_obj)

                self.create_book(book, authors, categories)

        json_file.close()
