from django import forms

from .models import poojatype_model


class poojatype_form(forms.ModelForm):


    class Meta:
        model=poojatype_model
        fields=('Pooja_type','Photo')