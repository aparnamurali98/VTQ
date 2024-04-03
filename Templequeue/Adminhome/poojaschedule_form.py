from django import forms

from .models import poojaschedule_model


class schedule_form(forms.ModelForm):

    class Meta:
        model=poojaschedule_model
        fields=('Timings','poojaid','dayid')