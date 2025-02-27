from django import forms

from .models import poojatype_model


class poojatype_form(forms.ModelForm):
    Pooja_type = forms.CharField(label='DEITIES')
    class Meta:
        model=poojatype_model
        fields=('Pooja_type',)