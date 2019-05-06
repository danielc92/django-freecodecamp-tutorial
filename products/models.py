from django.db import models

# Create your models here.
class Product(models.Model):
	# Note: a SERIAL PRIMARY KEY is created by default

	title = models.TextField()
	description = models.TextField()
	price = models.TextField()