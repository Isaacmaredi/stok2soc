import re
from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory

from crispy_forms.helper import FormHelper
# from crispy_forms.bootstrap import FormActions
# from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import Member, Beneficiary

class DateInput(forms.DateInput):
        input_type = 'date'

class MemberCreateForm(ModelForm):
    class Meta:
        model = Member
        fields = ('__all__')
        

        widgets = {
            'birth_date':DateInput(attrs={'placeholder':'yyyy-mm-dd'}), 
            'status_date':DateInput(),
            'cover_lapse_date':DateInput(),
            'middlename':forms.TextInput(attrs= {'placeholder':'Member seond name'}),  
            'address':forms.Textarea(attrs= {'rows':'3', 'placeholder':'Enter street address'}),    
        } 
    
    def __init__(self, *args, **kwargs):
        super(MemberCreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = True
        self.fields['middlename'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status_date'].widget.attrs['readonly'] = True
        self.fields['birth_date'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'  
        self.helper.field_class = 'col-lg-9'
    
        self.helper.form_show_labels = True
        
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

        
BeneficiaryFormset = inlineformset_factory(Member, 
                                                Beneficiary, 
                                                form = BeneficiaryCreateForm,
                                                fields='__all__',
                                                extra = 1)

class MemberSearchForm(forms.Form):
    name = forms.CharField(required=False)
    