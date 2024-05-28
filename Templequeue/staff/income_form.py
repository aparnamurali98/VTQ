from django import forms

from .models import incomes_model


class incomes_form(forms.ModelForm):
    widgets = {
        'income_date': forms.DateInput(attrs={'type': 'date'}),
    }

    class Meta:
        model=incomes_model
        fields=('income_typeid','income_date','Amount','Narration')
        widgets = {
            'income_date': forms.DateInput(attrs={'type': 'date'}),
        }