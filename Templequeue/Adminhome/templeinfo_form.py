from django import forms

from .models import templeinfo_model,pooja_model


class temple_form(forms.ModelForm):
    tname = forms.CharField(label='Temple Name')
    cotname= forms.CharField(label='Contact Name')
    contnum = forms.CharField(label='Contact Number')


    class Meta:
        model=templeinfo_model
        fields=('tname','address','discription','cotname','contnum','Photo','loc','Pooja')
