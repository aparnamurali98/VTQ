from django import forms

from .models import application_model


class application_form(forms.ModelForm):

    class Meta:
        model=application_model
        fields=('Resume',)