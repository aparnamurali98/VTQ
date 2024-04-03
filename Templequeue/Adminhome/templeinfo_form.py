from django import forms

from .models import templeinfo_model


class temple_form(forms.ModelForm):
    tname = forms.CharField(label='Temple Name')
    cotname= forms.CharField(label='Contact Name')
    class Meta:
        model=templeinfo_model
        fields=('tname','address','discription','cotname','Photo','loc')
