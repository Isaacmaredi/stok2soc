import re
from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory

from crispy_forms.helper import FormHelper
# from crispy_forms.bootstrap import FormActions
# from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import Meeting, MeetingAttendance, Funeral, FuneralAttendance

class DateInput(forms.DateInput):
        input_type = 'date'

class MeetingCreateForm(ModelForm):
    class Meta:
        model = Meeting  
        fields = ('__all__')
        

        widgets = {
            'date':DateInput(attrs={'placeholder':'yyyy-mm-dd'}),  
        } 
    
    def __init__(self, *args, **kwargs):
        super(MeetingCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'  
        self.helper.field_class = 'col-lg-9'
    
        self.helper.form_show_labels = True
        

class MeetingAttendanceCreateForm(ModelForm):
    class Meta:
        model = MeetingAttendance
        fields = ('__all__')
        exclude = ('meeting',)

        widgets = {
            'is_present':forms.CheckboxInput(attrs= {'checked':True}),  
        } 
    
    def __init__(self, *args, **kwargs):
        super(MeetingAttendanceCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'  
        self.helper.field_class = 'col-lg-9'

        # self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-sm-12'
    
        self.helper.form_show_labels = False
        
        # self.helper.form_class = 'form-horizontal'
    
        
MeetingAttendanceFormset = inlineformset_factory(Meeting, 
                                                MeetingAttendance, 
                                                MeetingAttendanceCreateForm,
                                                fields='__all__',
                                                extra = 5)


class FuneralCreateForm(ModelForm):
    class Meta:
        model = Funeral
        fields = ('__all__')
        

        widgets = {
            'date':DateInput(attrs={'placeholder':'yyyy-mm-dd'}), 
            'host':forms.TextInput(attrs= {'placeholder':'Select deceased member'}), 
        } 
    
    def __init__(self, *args, **kwargs):
        super(FuneralCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'  
        self.helper.field_class = 'col-lg-9'
    
        self.helper.form_show_labels = True
        

class FuneralAttendanceCreateForm(ModelForm):
    class Meta:
        model = FuneralAttendance
        fields = ('__all__')
        exclude = ('funeral',)

        widgets = {
            'is_present':forms.CheckboxInput(attrs= {'checked':True}),  
        } 
    
    def __init__(self, *args, **kwargs):
        super(FuneralAttendanceCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'  
        self.helper.field_class = 'col-lg-9'

        # self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-sm-12'
    
        self.helper.form_show_labels = False
        
        # self.helper.form_class = 'form-horizontal'
    
        
MeetingAttendanceFormset = inlineformset_factory(Meeting, 
                                                MeetingAttendance, 
                                                MeetingAttendanceCreateForm,
                                                fields='__all__',
                                                extra = 5)

FuneralAttendanceFormset = inlineformset_factory(Funeral,
                                                FuneralAttendance,
                                                FuneralAttendanceCreateForm,
                                                fields='__all__',
                                                extra = 6,
                                                ) 
        

class MeetingSearchForm(forms.Form):
    name = forms.CharField(required=False)
    