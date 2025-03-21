from django import forms

from .models import pooja_model


class pooja_form(forms.ModelForm):
    pname = forms.CharField(label='Pooja Name')

    class Meta:
        model=pooja_model
        fields=('poojatypeid','pname','desc','amount','Photo')