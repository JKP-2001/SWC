from django.db import models

# Create your models here.
# class Shop(models.Model):
# 	name=models.CharField(max_length=200)
# 	img=models.ImageField(upload_to='static')
# 	desc=models.TextField()
# 	price =models.IntegerField()
# 	offer=models.BooleanField(default=False)

class Shops(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='static')
	desc=models.TextField()
	price =models.IntegerField()
	offer=models.BooleanField(default=False)