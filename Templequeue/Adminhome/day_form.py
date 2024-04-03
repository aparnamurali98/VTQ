from django import forms

from .models import day_model


class day_form(forms.ModelForm):
    class Meta:
        model=day_model
        fields=('id','day')