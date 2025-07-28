from django import forms


from Adminhome.models import templeinfo_model



class district_form(forms.ModelForm):


    class Meta:
        model=templeinfo_model
        fields=('id','District')
