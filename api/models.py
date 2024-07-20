from django.db import models

# Create your models here.

class Book(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title