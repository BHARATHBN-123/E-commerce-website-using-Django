from django.db import models

# Create your models here.
class product_db(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=220)
    price = models.IntegerField()