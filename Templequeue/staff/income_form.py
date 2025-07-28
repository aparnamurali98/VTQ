from django import forms

from .models import incomes_models, income_model
from datetime import date

class incomes_form(forms.ModelForm):


    class Meta:
        model=incomes_models
        fields=('income_typeid','income_date','Amount','Narration')
        widgets = {
            'income_date': forms.DateInput(attrs={'type': 'date', 'value': date.today().isoformat(), 'max': date.today().isoformat(), 'min': date.today().isoformat()}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude "Online Pooja Booking" (assuming ID is 10)
        self.fields['income_typeid'].queryset = income_model.objects.exclude(id=1)