from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_published = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('author',)
        verbose_name = 'Книгa'
        verbose_name_plural = 'Книги'

