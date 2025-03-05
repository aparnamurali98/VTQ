from django import forms

from .models import Expense_models
from datetime import date



class expense_form(forms.ModelForm):

    class Meta:
        model=Expense_models
        fields=('Expense_typeid','Expense_date','Amount','Narration')
        widgets = {
            'Expense_date': forms.DateInput(attrs={'type': 'date', 'value': date.today().isoformat(), 'max': date.today().isoformat(), 'min': date.today().isoformat()}),
        }