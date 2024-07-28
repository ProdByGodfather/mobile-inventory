from django.db import models
from colorfield.fields import ColorField

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nationality = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    color = ColorField(default='#FF0000')
    screen_size = models.DecimalField(decimal_places=2, max_digits=10)
    STATUS_CHOICES = [
        ('available', 'موجود'),
        ('unavailable', 'ناموجود'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    manufacturing_country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand.name} {self.model}"