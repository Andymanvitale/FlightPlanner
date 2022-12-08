from django import forms
from .models import airportModel


class airportRoute(forms.ModelForm):
    startApt = forms.CharField(label = 'Starting Airport', max_length = 3)
    endApt = forms.CharField(label = 'Destination', max_length = 3)
    class Meta:
        fields = ['text']
        widgets = {
            'text':forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'placeholder': 'Type in Route'
            }),
        }

class AptForm(forms.ModelForm):
    class Meta:
        model = airportModel
        fields = '__all__'