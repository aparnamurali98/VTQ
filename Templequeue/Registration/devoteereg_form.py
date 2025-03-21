from django import forms

from .models import devotee_model



gender=[('M','Male'),('F','Female'),('T','Transgender')]



class devo_form(forms.ModelForm):
    gender = forms.CharField( widget=forms.RadioSelect(choices=gender))
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    class Meta:
        model=devotee_model
        fields=('dname','address','age','gender','email','mobile','District')