from django import forms
from django.core.validators import RegexValidator
from .models import enquiry_model


class enquiry_form(forms.ModelForm):
    Mobile = forms.CharField(
        label='Mobile',
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message='Enter a valid 10-digit mobile number starting with 6-9'
            )
        ]
    )

    class Meta:
        model=enquiry_model
        fields=('Name','Email','Mobile','Query')