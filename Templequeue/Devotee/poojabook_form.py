from django import forms

from .models import poojabook_model


class poojabook_form(forms.ModelForm):

    class Meta:
        model=poojabook_model
        fields=('Devotee','pooja','Name','star','Status')