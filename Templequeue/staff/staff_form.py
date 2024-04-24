from django import forms

from Adminhome.models import staff_model


class DateInput(forms.DateInput):
    input_type='date'
gender=[('M','Male'),('F','Female')]
class staff_form(forms.ModelForm):
    dob = forms.DateField(widget=DateInput,label='Date Of Birth')
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=gender))
    sname = forms.CharField(label='Staff Name')
    email= forms.EmailField(label='Email')
    mobile= forms.IntegerField(label='Phone Number')
    photo= forms.FileField(label='Photo')
    age= forms.IntegerField(label='Age')

    class Meta:
        model=staff_model
        fields=('sname','address','email','mobile','photo','dob','age','gender')