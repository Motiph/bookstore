from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(BaseModel):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return self.title
