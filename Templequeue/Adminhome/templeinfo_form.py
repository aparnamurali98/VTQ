from django import forms
from django.core.validators import RegexValidator

from .models import templeinfo_model,pooja_model


class temple_form(forms.ModelForm):
    tname = forms.CharField(label='Temple Name')
    cotname= forms.CharField(label='Contact Name')
    contnum = forms.CharField(
        label='Contact Number',
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message='Enter a valid 10-digit phone number starting with 6-9'
            )
        ]
    )
    Photo = forms.ImageField(label='Photo', required=True)


    class Meta:
        model=templeinfo_model
        fields=('tname','address','discription','cotname','contnum','Photo','loc','Pooja','Priest','District')
