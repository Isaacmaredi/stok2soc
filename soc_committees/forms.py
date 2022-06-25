import re
from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory

from crispy_forms.helper import FormHelper
# from crispy_forms.bootstrap import FormActions
# from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import Committee, Incumbent

class DateInput(forms.DateInput):
        input_type = 'date'

class CommitteeCreateForm(ModelForm):
    class Meta:
        model = Committee
        fields = ['name','shortname','term_starts','term_ends',]
        
        widgets = {
            'term_starts':DateInput(attrs={'placeholder':'yyyy-mm-dd'}), 
            'term_ends':DateInput(),
        } 
    
    def __init__(self, *args, **kwargs):
        super(CommitteeCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'  
        self.helper.field_class = 'col-lg-10'
    
        self.helper.form_show_labels = False
        
class DateInput(forms.DateInput):
        input_type = 'date'

class IncumbentCreateForm(ModelForm):
    class Meta:
        model = Incumbent
        fields = ['committee','member','portfolio',]
        
    
    def __init__(self, *args, **kwargs):
        super(IncumbentCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-sm-12'
    
        self.helper.form_show_labels = False

        
IncumbentFormset = inlineformset_factory(Committee, 
                                                Incumbent, 
                                                IncumbentCreateForm,
                                                extra = 4)

class CommitteeSearchForm(forms.Form):
    name = forms.CharField(required=False)
    