from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
# from crispy_forms.bootstrap import FormActions
# from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import Beneficiary



class DateInput(forms.DateInput):
        input_type = 'date'

class BeneficiaryCreateForm(ModelForm):
    class Meta:
        model = Beneficiary
        fields = ('__all__')
        

        widgets = {
            'birth_date':DateInput(attrs={'placeholder':'yyyy-mm-dd'}), 
            'paid_date':DateInput(),
            'full_name':forms.TextInput(attrs= {'placeholder':'Full names as per ID'}),  
        } 
    
    def __init__(self, *args, **kwargs):
        super(BeneficiaryCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
    
        self.helper.form_show_labels = True
        
        
        
    

        
        
    