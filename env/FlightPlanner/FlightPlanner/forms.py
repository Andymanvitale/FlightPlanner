from django import forms


class airports(forms.Form):
    startApt = forms.CharField(label = 'startapt', max_length = 3)
    endApt = forms.CharField(label = 'endapt', max_length = 3)

class airportRoute(forms.ModelForm):
    class Meta:
        fields = ['text']
        widgets = {
            'text':forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'placeholder': 'Type in Route'
            }),
        }