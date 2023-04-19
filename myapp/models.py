from django.db import models

# Create your models here.

class Product(models.Model):
    image=models.FileField(upload_to='',blank=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    qty=models.IntegerField()
    price=models.FloatField()
    date=models.DateField()