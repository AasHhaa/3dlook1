from django.utils import timezone
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='photos')
    rotate_duration = models.FloatField()
    modified = models.BooleanField(default=False)

    def __str__(self):
        return f"name - {self.name}"
