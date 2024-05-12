from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from accaunts.models import CostumerUsers
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class BookCategory(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        db_table = 'bookcategory'

    def __str__(self):
        return self.category


class Language(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/books/', default='default_img/book_img.jpg')
    page = models.IntegerField()
    book_lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title


class BooksAuthor(models.Model):
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'BooksAuthor'

    def __str__(self):
        return str(self.book)


class Review(models.Model):
    comment = models.TextField()
    star_given = models.IntegerField(
        default=0,
        validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(CostumerUsers, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.star_given}{self.user.username}{self.book.title}'

