from django import forms

from .models import transtype_model


class transf_form(forms.ModelForm):
    transmode= forms.CharField(label='Transation Mode')

    class Meta:
        model=transtype_model
        fields=('id','transmode')