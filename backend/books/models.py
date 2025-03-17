from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    description = models.TextField()
    price=models.CharField(max_length=10)

    def __str__(self):
        return self.title
