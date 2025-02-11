from django import forms

from .models import incomes_models


class incomes_form(forms.ModelForm):
    widgets = {
        'income_date': forms.DateInput(attrs={'type': 'date'}),
    }

    class Meta:
        model=incomes_models
        fields=('income_typeid','income_date','Amount','Narration','Temple_name')
        widgets = {
            'income_date': forms.DateInput(attrs={'type': 'date'}),
        }