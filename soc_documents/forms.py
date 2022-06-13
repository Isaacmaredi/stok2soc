from django import forms
from .models import Minutes

class DateInput(forms.DateInput):
        input_type = 'date'

class MinutesForm(forms.ModelForm):
    class Meta:
        model = Minutes
        fields = '__all__'
        exclude =('uploaded_by',)
        
       