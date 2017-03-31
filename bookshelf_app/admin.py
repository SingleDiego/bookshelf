from django.contrib import admin
from bookshelf_app.models import Book
from bookshelf_app.models import Book, BookID

admin.site.register(Book)
admin.site.register(BookID)
