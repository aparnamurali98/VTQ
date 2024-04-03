from django import forms

from .models import location_model


class loca_form(forms.ModelForm):
    locname = forms.CharField(label='Location')


    class Meta:
        model=location_model
        fields=('locname','dist')