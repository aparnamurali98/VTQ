from django import forms

from .models import priest_model


class prie_form(forms.ModelForm):
    Pname= forms.CharField(label='Priest Name')

    class Meta:
        model=priest_model
        fields=('Pname','Age','Address','loc','Jobtype','Phone','Email','Experience')