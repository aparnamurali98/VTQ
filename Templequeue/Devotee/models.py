import django
from django.db import models
from Adminhome.models import careers_model
from Registration.models import devotee_model
from Adminhome.models import pooja_model
from Adminhome.models import staff_model,templeinfo_model


# Create your models here.
class application_model(models.Model):
    Devotee_id=models.ForeignKey(devotee_model,on_delete=models.CASCADE)
    careerid=models.ForeignKey(careers_model,on_delete=models.CASCADE)
    Resume=models.FileField(upload_to="photos", blank=True)
    Status=models.CharField(max_length=30,default='active')
    Application_date= models.DateTimeField(max_length=10,default=django.utils.timezone.now)
    class Meta:
        db_table='Application'




class bookingpooja_model(models.Model):
    Devotee=models.ForeignKey(devotee_model,on_delete=models.CASCADE)
    Booking_type=models.CharField(max_length=30,default='online')
    Want_date = models.DateField(null=True)
    booked_date= models.DateTimeField(max_length=10,default=django.utils.timezone.now)
    Total_amount= models.IntegerField(null=True)
    Status=models.CharField(max_length=30,default='New')
    staff = models.ForeignKey(staff_model, on_delete=models.CASCADE,null=True)
    Temple_name = models.ForeignKey(templeinfo_model, on_delete=models.CASCADE, null=True)
    Mail_status=models.CharField(max_length=6,null=True)

    class Meta:
        db_table='Bokking_Pooja'
CARD_TYPE=(
    ('select','SELECT'),
    ('credit card','CREDIT CARD'),
    ('debit card','DEBIT CARD'),
    ('upi','UPI'),
    ('netbanking','NETBANKING'),
)

class poojabook_model(models.Model):
    Devotee=models.ForeignKey(devotee_model,on_delete=models.CASCADE)
    booking=models.ForeignKey(bookingpooja_model,on_delete=models.CASCADE,null=True)
    pooja=models.ForeignKey(pooja_model,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=30,null=True)
    star = models.CharField(max_length=30)
    Status=models.CharField(max_length=30,default='cart')


    class Meta:
        db_table='Pooja_Book'
class payment_model(models.Model):
    poojabook = models.ForeignKey(bookingpooja_model, on_delete=models.CASCADE)
    Payment_date=models.DateTimeField(max_length=10,default=django.utils.timezone.now)
    card_type=models.CharField(max_length=20,choices=CARD_TYPE,default='SELECT')
    card_holder_name = models.CharField(max_length=30)
    Card_number= models.BigIntegerField()
    card_exp_date= models.CharField(max_length=15)
    cvv_number = models.IntegerField()
    Status=models.CharField(max_length=30,default='paid')
    Total_amount= models.CharField(max_length=20)

    class Meta:
        db_table='payment'


