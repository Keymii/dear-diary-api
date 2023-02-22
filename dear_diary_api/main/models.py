from django.db import models

# Create your models here.
class userLogin(models.Model):
    name=models.CharField(max_length=200)

    userid=models.CharField(max_length=14,primary_key=True)
    pswd=models.CharField(max_length=30)

    def __str__(self):
        return self.userid