from django import forms

from .models import specialday_model
from datetime import date



class specialday_form(forms.ModelForm):

    class Meta:
        model=specialday_model
        fields=('Title','Description','From_date','To_date')
        widgets = {
            'From_date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()}),
            'To_date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
        }
