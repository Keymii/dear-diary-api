from django.db import models

# Create your models here.
class userLogin(models.Model):
    userid=models.CharField(max_length=14,primary_key=True)
    pswd=models.CharField(max_length=30)
    