from django.contrib.auth.models import User
from django.db import models

from Adminhome.models import location_model,distric_model


# Create your models here.
class devotee_model(models.Model):
    dname = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    email = models.EmailField('Email Id', blank=True)
    mobile = models.BigIntegerField()
    District = models.ForeignKey(distric_model, on_delete=models.CASCADE,null=True)
    login=models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
         return self.dname



class role_model(models.Model):
    login = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    roletype=models.CharField(max_length=10)
class enquiry_model(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField('Email Id', blank=True)
    Mobile = models.BigIntegerField()
    Query = models.TextField(max_length=200)
    Status= models.CharField(max_length=50,default='new')

    class Meta:
        db_table = "Enquiry"