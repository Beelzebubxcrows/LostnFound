from django import forms
from lost.models import Lost,Found


class formlost(forms.ModelForm):
    class Meta:
        model= Lost
        fields = '__all__'



class formfound(forms.ModelForm):
    class Meta:
        model= Found
        fields='__all__'



   

