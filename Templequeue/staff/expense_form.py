from django import forms

from .models import Expense_models


class expense_form(forms.ModelForm):
    widgets = {
        'Expense_date': forms.DateInput(attrs={'type': 'date'}),
    }

    class Meta:
        model=Expense_models
        fields=('Expense_typeid','Expense_date','Amount','Narration')
        widgets = {
            'Expense_date': forms.DateInput(attrs={'type': 'date'}),
        }