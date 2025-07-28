from django import forms
from django.core.validators import MinValueValidator

from .models import pooja_model


class pooja_form(forms.ModelForm):
    pname = forms.CharField(label='Pooja Name')
    amount = forms.DecimalField(
        label='Amount',
        min_value=1,
        error_messages={'min_value': 'Amount must be greater than 0'}
    )
    Photo = forms.ImageField(required=True, label='Photo')

    class Meta:
        model=pooja_model
        fields=('poojatypeid','pname','desc','amount','Photo')