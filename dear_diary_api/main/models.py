from django.db import models

# Create your models here.
class userLogin(models.Model):
    name=models.CharField(max_length=200)
    userid=models.CharField(max_length=14,primary_key=True)
    pswd=models.CharField(max_length=30)
    def __str__(self):
        return self.userid
    
class MasterTable(models.Model):
    userid = models.ForeignKey(userLogin,on_delete=models.CASCADE,default=0)
    section = models.CharField('Section',max_length=50)
    page = models.CharField('Page',max_length=50)
    data = models.TextField() 
    def __str__(self):
        return self.userid.userid
    

    