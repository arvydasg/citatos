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
        ordering = ['birth_date']

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
    published = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.quote_text

    class Meta:
        ordering = ['published']
