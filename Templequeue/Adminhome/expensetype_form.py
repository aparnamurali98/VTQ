from django import forms

from .models import expense_model


class expense_form(forms.ModelForm):
    Exptype= forms.CharField(label='Expense Type Name')

    class Meta:
        model=expense_model
        fields=('id','Exptype')