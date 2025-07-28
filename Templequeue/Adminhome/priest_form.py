from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from .models import priest_model


class prie_form(forms.ModelForm):
    Pname= forms.CharField(label='Priest Name')
    Age = forms.IntegerField(
        label='Age',
        validators=[
            MinValueValidator(18, message="Age must be at least 18"),
            MaxValueValidator(99, message="Age must be less than 100")
        ]
    )
    Phone = forms.CharField(
        label='Phone',
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message='Enter a valid 10-digit phone number starting with 6-9'
            )
        ]
    )

    class Meta:
        model=priest_model
        fields=('Pname','Age','Address','dist','Jobtype','Phone','Experience')