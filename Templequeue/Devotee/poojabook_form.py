from django import forms

from .models import poojabook_model


class poojabook_form(forms.ModelForm):
    STAR_CHOICES = [
        ('Ashwathi', 'Ashwathi'),
        ('Bharani', 'Bharani'),
        ('Karthika', 'Karthika'),
        ('Rohini', 'Rohini'),
        ('Makayiram', 'Makayiram'),
        ('Thiruvathira', 'Thiruvathira'),
        ('Punartham', 'Punartham'),
        ('Pooyam', 'Pooyam'),
        ('Ayilyam', 'Ayilyam'),
        ('Makam', 'Makam'),
        ('Pooram', 'Pooram'),
        ('Uthram', 'Uthram'),
        ('Atham', 'Atham'),
        ('Chithira', 'Chithira'),
        ('Chothi', 'Chothi'),
        ('Visakham', 'Visakham'),
        ('Anizham', 'Anizham'),
        ('Thrikketta', 'Thrikketta'),
        ('Moolam', 'Moolam'),
        ('Pooradam', 'Pooradam'),
        ('Uthradam', 'Uthradam'),
        ('Thiruvonam', 'Thiruvonam'),
        ('Avittam', 'Avittam'),
        ('Chathayam', 'Chathayam'),
        ('Pooruruttathi', 'Pooruruttathi'),
        ('Uthrattathi', 'Uthrattathi'),
        ('Revathi', 'Revathi'),
    ]

    star = forms.ChoiceField(choices=STAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model=poojabook_model
        fields=('Devotee','pooja','Name','star','Status')