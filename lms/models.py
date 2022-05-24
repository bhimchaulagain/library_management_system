from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.
STATUS = (
    ('a', "Available"),
    ('b', "Issued")
)
class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll_no = models.CharField(max_length = 4)
    contact_no = models.CharField(max_length = 100)


    def __str__(self):
        return str(self.roll_no)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    unique_id = models.PositiveIntegerField()

    def __str__(self):
        return str(self.title) + " ["+str(self.unique_id) + "]"


class BooksIssued(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title) + " [" + str(self.unique_id) + "]"

    def expiry_date(self):
        return datetime.today() + timedelta(days = 30)


class BooksReturned(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    return_date = models.DateField(null=True, blank=True)
