from django.db import models

class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.TextField()
    gender=models.CharField(max_length=8)
    phone=models.IntegerField()
    postal=models.IntegerField()

# Create your models here.
