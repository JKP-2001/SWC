

# Create your models here.
from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=120)
	email=models.EmailField(max_length=120)
	phone=models.CharField(max_length=12)
	desc=models.TextField()
	date=models.DateField()
	def __str__(self):
		return self.name
class Product(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='static')
	desc=models.TextField()
	price =models.IntegerField()
	offer=models.BooleanField(default=False)
