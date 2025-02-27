from django import forms

from .models import careers_model


Status=[('A','Active'),('I','Inactive')]
class careers_form(forms.ModelForm):
    Status = forms.CharField(label='Status', widget=forms.RadioSelect(choices=Status))
    Adddate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Add Date'
    )
    class Meta:
        model=careers_model
        fields=('Refno','Jobtitle','Notification','Notification_file','Adddate')