from django.db import models

# Create your models here.
class MasterTable(models.Model):
    userdataid =  models.IntegerField(primary_key='True')
    user = models.CharField('User Id',max_length=50)
    section = models.CharField('Section',max_length=50)
    page = models.CharField('Page',max_length=50)
    data = models.CharField(max_length=500) 
    def __int__(self):
        return self.userdataid
    
    
    