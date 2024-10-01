from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    published_date = models.DateField()

    def __str__(self) -> str:
        return self.title
