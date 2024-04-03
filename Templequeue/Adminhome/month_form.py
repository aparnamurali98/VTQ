from django import forms

from .models import month_model


class month_form(forms.ModelForm):
    class Meta:
        model=month_model
        fields=('id','Month')