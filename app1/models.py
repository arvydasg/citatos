from django.db import models

class Quote(models.Model):
    quote_author = models.CharField(max_length=100)   # foreign key
    quote_category = models.CharField(max_length=100) # foreign key
    quote_text = models.TextField()
    quote_published = models.DateTimeField("date published")

    def __str__(self):
        return self.quote_text
