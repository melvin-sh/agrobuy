from django.db import models

# Create your models here.

class Farmer(models.Model):
    name = models.CharField(max_length=50)
    
    address = models.CharField(max_length=250)
    mobile = models.DecimalField(max_digits=10, decimal_places=0)
