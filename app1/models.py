from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=50, null=True)
    bio = models.TextField()
    birth_date = models.CharField(max_length=30, null=True)
    death_date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    name = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author, null=True, on_delete= models.SET_NULL)
    publihed = models.CharField(max_length=30, null=True)
    pages = models.CharField(max_length=30, null=True)
    read_in = models.CharField(max_length=100, null=True)
    summary = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Quote(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete= models.SET_NULL)
    category = models.ManyToManyField(Category)
    text = models.TextField(null=True)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete= models.SET_NULL)
    published = models.DateTimeField("date published", auto_now_add=True)


    def __str__(self):
        return self.text

    class Meta:
        ordering = ['published']
