from django import forms

from .models import careers_model


class careers_form(forms.ModelForm):
    class Meta:
        model=careers_model
        fields=('Refno','Jobtitle','Notification','notifyfile','adddate')