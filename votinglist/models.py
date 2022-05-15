from django.db import models
class Votlins(models.Model):
    Candidates=models.TextField()
    votes=models.IntegerField()
    email=models.EmailField()
    news_image=models.FileField(upload_to="logo/",max_length=250,null=True,default=None)
# Create your models here.
