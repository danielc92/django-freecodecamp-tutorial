from django.db import models

# Create your models here.
class Product(models.Model):

    # Note: a SERIAL PRIMARY KEY is created by default
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    summary = models.TextField(default='This product has not been given a summary.')
    created_at = models.DateField(auto_now=True)