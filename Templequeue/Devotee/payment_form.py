from django import forms

from .models import payment_model


class payment_form(forms.ModelForm):
    cvv_number = forms.CharField(max_length=10, widget=forms.PasswordInput)

    class Meta:
        model=payment_model
        fields=('card_type','card_holder_name','Card_number','card_exp_date','Total_amount')