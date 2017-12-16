from django.db import models

# Create your models here.

class Book (models.Model):
    writer = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    book_cover = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + " - " + self.writer



class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    chapter_title = models.CharField(max_length=250)
    page_number = models.CharField(max_length=250)
