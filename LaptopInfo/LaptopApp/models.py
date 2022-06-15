from django.db import models

brand = [('Dell','Dell'), ('HP','HP'),('Lenovo','Lenovo'),('Acer','Acer')]
class Laptop(models.Model):
    laptop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    brand = models.CharField(max_length=80, choices=brand)
    ram = models.CharField(max_length=20)
    rom = models.CharField(max_length=20)
    HDD = models.CharField(max_length=20)
    SSD = models.CharField(max_length=20)
    price = models.FloatField()




# Create your models here.
