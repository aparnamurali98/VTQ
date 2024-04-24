from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class distric_model(models.Model):
    distname=models.CharField(max_length=40)
    class Meta:
        db_table='District'

    def __str__(self):
         return self.distname


class location_model(models.Model):
    locname=models.CharField(max_length=30)
    dist=models.ForeignKey(distric_model,on_delete=models.CASCADE)
    class Meta:
        db_table="location"
    def __str__(self):
         return self.locname

class staff_model(models.Model):
    sname=models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    email=models.EmailField('Email Id',blank=True)
    mobile = models.IntegerField()
    photo = models.FileField(upload_to="photos", blank=True)
    dob = models.DateField(max_length=8)
    age=models.IntegerField()
    gender=models.CharField(max_length=7)
    login =models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    class Meta:
        db_table="staff"



class templeinfo_model(models.Model):
    tname=models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    discription = models.TextField(max_length=100)
    cotname=models.CharField(max_length=30)
    Photo=models.FileField(upload_to="photos", blank=True)
    loc=models.ForeignKey(location_model,on_delete=models.CASCADE)
    class Meta:
        db_table="templeinfo"

class priest_model(models.Model):
    Pname=models.CharField(max_length=30)
    Age = models.IntegerField()
    Address = models.TextField(max_length=100)
    loc = models.ForeignKey(location_model, on_delete=models.CASCADE)
    Jobtype=models.CharField(max_length=30)
    Phone = models.BigIntegerField()
    Email = models.EmailField('Email Id', blank=True)
    Experience=models.IntegerField()
    class Meta:
        db_table="hindu_priest"
    def __str__(self):
         return self.Pname
class poojatype_model(models.Model):
    Pooja_type=models.CharField(max_length=20)
    Photo = models.FileField(upload_to="photos", blank=True)

    class Meta:
        db_table="poojaTypecategory_model"
    def __str__(self):
         return self.Pooja_type


class pooja_model(models.Model):
    poojatypeid = models.ForeignKey(poojatype_model, on_delete=models.CASCADE, null=True)
    pname=models.CharField(max_length=30)
    desc= models.TextField(max_length=100)
    priestid =models.ForeignKey(priest_model, on_delete=models.CASCADE)
    amount = models.IntegerField()
    active=models.CharField(max_length=30)
    class Meta:
        db_table="pooja_type"
    def __str__(self):
         return self.pname
class day_model(models.Model):
    day=models.CharField(max_length=30)
    class Meta:
        db_table="day"

    def __str__(self):
        return self.day
class transtype_model(models.Model):
    transmode = models.CharField(max_length=50)
    class Meta:
        db_table="transfer_type"
class income_model(models.Model):
    inctype = models.CharField(max_length=50)
    class Meta:
        db_table="income_type"
class month_model(models.Model):
    Month=models.CharField(max_length=30)
    class Meta:
        db_table="Month"
class expense_model(models.Model):
    Exptype=models.CharField(max_length=30)
    class Meta:
        db_table="Expense_type"


class poojaschedule_model(models.Model):
    poojaid =models.ForeignKey(pooja_model, on_delete=models.CASCADE)
    dayid =models.ForeignKey(day_model, on_delete=models.CASCADE)
    Timings=models.CharField(max_length=8)
    class Meta:
        db_table="pooja_schedule"
class specialday_model(models.Model):
    Title = models.CharField(max_length=30)
    Description=models.TextField(max_length=100)
    From_date= models.DateField(max_length=10)
    To_date = models.DateTimeField(max_length=10)
    status=models.CharField(max_length=30,default='Inactive')
    class Meta:
        db_table="special_day"

class careers_model(models.Model):
    Refno = models.IntegerField()
    Jobtitle = models.CharField(max_length=30)
    Notification = models.CharField(max_length=30)
    notifyfile = models.CharField(max_length=50)
    adddate=models.DateField(max_length=10)
    Status = models.CharField(max_length=50)



    class Meta:
        db_table = "careers"
class darshan_model(models.Model):
    Timings = models.CharField(max_length=8)

    class Meta:
        db_table = "darshan_timing"


