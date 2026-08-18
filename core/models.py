from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
