from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
    img_url = models.URLField(max_length=2083)
    