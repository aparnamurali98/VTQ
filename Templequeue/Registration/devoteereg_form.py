from django import forms
from django.core.validators import RegexValidator
from .models import devotee_model



gender=[('M','Male'),('F','Female'),('T','Transgender')]



class devo_form(forms.ModelForm):
    gender = forms.CharField( widget=forms.RadioSelect(choices=gender))
    username = forms.CharField(max_length=20)
    password = forms.CharField(
        max_length=10,
        widget=forms.PasswordInput,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                message="Password must be minimum eight characters, at least one letter and one number",
                code='invalid_password'
            )
        ]
    )

    confirm_password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput
    )
    class Meta:
        model=devotee_model
        fields=('dname','address','age','gender','email','mobile','District')