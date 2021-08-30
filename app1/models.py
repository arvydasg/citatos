from django.db import models

class Citata(models.Model):
    citata_author = models.CharField(max_length=255)
    citata_category = models.CharField(max_length=255)
    citata_quote = models.TextField()
    citata_published = models.DateTimeField("date published")

    def __str__(self):
        return self.citata_title
