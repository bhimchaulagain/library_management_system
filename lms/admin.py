from django.contrib import admin
from.models import Student, Book, BooksIssued, BooksReturned
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(BooksIssued)
admin.site.register(BooksReturned)

# Register your models here.
