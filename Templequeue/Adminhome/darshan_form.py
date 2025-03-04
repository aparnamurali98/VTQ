from django import forms

from .models import darshan_model


class darsh_form(forms.ModelForm):
    class Meta:
        model=darshan_model
        fields=('id','Day','Timings')