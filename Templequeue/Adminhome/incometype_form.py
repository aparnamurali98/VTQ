from django import forms

from .models import income_model


class income_form(forms.ModelForm):
    inctype= forms.CharField(label='Income Type')

    class Meta:
        model=income_model
        fields=('id','inctype')