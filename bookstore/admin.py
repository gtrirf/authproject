from django.contrib import admin
from .models import BookCategory, Language, Books, Author, BooksAuthor, Review

admin.site.register(BookCategory)
admin.site.register(Language)
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(BooksAuthor)
admin.site.register(Review)