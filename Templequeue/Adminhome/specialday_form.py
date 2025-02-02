from django import forms

from .models import specialday_model


class specialday_form(forms.ModelForm):

    class Meta:
        model=specialday_model
        fields=('Title','Description','From_date','To_date','Temple_name')