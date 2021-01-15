from django import forms
from django.contrib.admin import widgets
from .models import InputsContainer

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PlotInputs(forms.ModelForm):
    """A form to store the messages sent by visitors"""
    starting_amount = forms.FloatField(label='Starting amount ', min_value=0, initial=5000)
    cagr = forms.FloatField(label='Compound annual growth rate ', min_value=0, initial=20)
    num_years = forms.IntegerField(label='Investment period in years ', min_value=0, initial=20)    
    beginning_year = forms.IntegerField(label='Beginning year ', min_value=1900, initial=2021, required=False)
    annual_topup = forms.FloatField(label='Annual investment ', initial=1000, required=False)    
    topup_years = forms.IntegerField(label='Annual investment duration ', initial=5, required=False)

    class Meta:
        model = InputsContainer 
        fields = ('starting_amount', 'cagr', 'num_years', 'beginning_year','annual_topup','topup_years')
        
