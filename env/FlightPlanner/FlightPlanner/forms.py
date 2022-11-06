from django import forms


class airports(forms.Form):
    startApt = forms.CharField(label = 'startapt', max_length = '3')
    endApt = forms.CharField(label = 'endapt', max_length = '3')
