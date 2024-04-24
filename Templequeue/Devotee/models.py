import django
from django.db import models

from Adminhome.models import careers_model
from Registration.models import devotee_model


# Create your models here.
class application_model(models.Model):
    Devotee_id=models.ForeignKey(devotee_model,on_delete=models.CASCADE)
    careerid=models.ForeignKey(careers_model,on_delete=models.CASCADE)
    Resume=models.FileField(upload_to="photos", blank=True)
    Status=models.CharField(max_length=30,default='active')
    Application_date= models.DateTimeField(max_length=10,default=django.utils.timezone.now)
    class Meta:
        db_table='Application'
