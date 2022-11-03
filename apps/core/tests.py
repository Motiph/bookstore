import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Author, Book, Category


class AuthorTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.author = Author(
            first_name='Edwin',
            last_name='Gutierrez'
        )
        self.author.save()

    def test_create_author(self):
        response = self.client.post(
            '/api/authors/', {
                'first_name': 'William',
                'last_name': 'Shakespeare'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/api/authors/', {
                'first_name': 'Stephen',
                'last_name': 'King'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/api/authors/')

        self.assertEqual(len(response.data), 3)

    
    def test_update_author(self):
        response = self.client.put(
            f'/api/authors/{self.author.id}/', {
                'first_name': 'Edwin',
                'last_name': 'Mendoza'
            }
        )

        self.assertEquals(response.data.get('last_name'), 'Mendoza')

class BookTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.author = Author(
            first_name='William',
            last_name='Shakespeare'
        )
        self.author.save()

        self.category = Category(
            name='JAVA'
        )
        self.category.save()


        self.book = Book(
            title='Java Network Programming, Second Edition',
            isbn='188477749X',
            status='PUBLISH',
            page_count=860,
            thumbnail_url='https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/hughes.jpg'
        )
        self.book.save()
        self.book.authors.add(self.author)
        self.book.categories.add(self.category)



    def test_book_create(self):
        response = self.client.post(
            '/api/books/', {
                'title': 'Struts in Action',
                'isbn': '1932394249',
                'authors': [self.author.id],
                'status': 'PUBLISH',
                'categories': [self.category.id],
                'page_count': 672,
                'thumbnail_url': 'https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/husted.jpg'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_book_update(self):
        response = self.client.put(
            f'/api/books/{self.book.id}/', {
                'title': 'New Book Title',
                'isbn': '1932394249',
                'authors': [self.author.id],
                'status': 'PUBLISH',
                'categories': [self.category.id],
                'page_count': 672,
                'thumbnail_url': 'https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/husted.jpg'
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title', None), 'New Book Title')

