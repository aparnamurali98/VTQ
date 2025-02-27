import django
from django.db import models

from Adminhome.models import income_model

from Registration.models import devotee_model

from Devotee.models import bookingpooja_model

from Adminhome.models import staff_model
from Adminhome.models import templeinfo_model


# Create your models here.


class incomes_models(models.Model):
    income_typeid = models.ForeignKey(income_model, on_delete=models.CASCADE)
    Devotee = models.ForeignKey( devotee_model, on_delete=models.CASCADE,null=True)
    income_date = models.DateTimeField(max_length=10,default=django.utils.timezone.now)
    Bookingpooja =models.ForeignKey( bookingpooja_model, on_delete=models.CASCADE,null=True)
    Amount=models.IntegerField()
    Narration=models.TextField(max_length=30,null=True)
    staff = models.ForeignKey(staff_model, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = "Staff_income_model"