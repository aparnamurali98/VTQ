from django import forms

from .models import enquiry_model


class enquiry_form(forms.ModelForm):

    class Meta:
        model=enquiry_model
        fields=('Name','Email','Mobile','Query')