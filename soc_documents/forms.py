from django import forms
from .models import Minutes, Policy

class DateInput(forms.DateInput):
        input_type = 'date'

class MinutesForm(forms.ModelForm):
    class Meta:
        model = Minutes
        fields = '__all__'
        exclude =('uploaded_by',)
        
class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = '__all__'
        exclude =('uploaded_by',)
        
    