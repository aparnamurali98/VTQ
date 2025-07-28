from django import forms
from django.core.validators import RegexValidator
from .models import staff_model
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type='date'

    def __init__(self, **kwargs):
        kwargs['attrs'] = {'max': timezone.now().date().strftime('%Y-%m-%d')}
        super().__init__(**kwargs)

gender=[('M','Male'),('F','Female')]
class staf_form(forms.ModelForm):
    dob = forms.DateField(widget=DateInput,label='Date Of Birth')
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=gender))
    sname = forms.CharField(label='Staff Name')
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    email= forms.EmailField(label='Email')
    # mobile= forms.IntegerField(label='Phone Number')
    mobile = forms.CharField(
        max_length=10,
        min_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Mobile number must be exactly 10 digits.",
                code='invalid_mobno'
            )
        ]
    )

    photo= forms.FileField(label='Photo')
    age = forms.CharField(
        max_length=2,
        min_length=1,
        validators=[
            RegexValidator(
                regex=r'^\d{2}$',
                message="Invalid Age.",
                code='invalid Age'
            )
        ]
    )
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
        model=staff_model
        fields=('sname','address','email','mobile','photo','dob','age','gender','Temple_name')

