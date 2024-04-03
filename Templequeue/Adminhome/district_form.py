from django import forms

from .models import distric_model


class dist_form(forms.ModelForm):
    distname=forms.CharField(label='District Name')
    class Meta:
        model=distric_model
        fields=('id','distname')
