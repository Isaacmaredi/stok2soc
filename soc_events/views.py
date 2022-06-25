from re import L
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView                             
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Meeting, MeetingAttendance, Funeral, FuneralAttendance
from .forms import (MeetingCreateForm, MeetingAttendanceCreateForm, 
                    FuneralCreateForm, FuneralAttendanceCreateForm,
                    MeetingAttendanceFormset,FuneralAttendanceFormset
                    )
from soc_documents.models import Minutes

# Meetings Views 

class MeetingList(ListView):
    model = Meeting
    context_object_name = 'meetings'
    template_name = 'soc_events/meeting_list.html'
    
    ordering = ['-date',]    
    
class MeetingAdminView(LoginRequiredMixin, ListView):
    model = Meeting
    context_object_name = 'meetings'
    template_name = 'soc_events/meeting_admin.html'


class MeetingDetail(DetailView):
    model = Meeting
    context_object_name = 'meeting'
    template_name = 'soc_events/meeting_detail.html'
    
class MeetingAdminDetailView(LoginRequiredMixin, DetailView):
    model = Meeting
    context_object_name = 'meeting'
    template_name = 'soc_events/meeting_admin_detail.html'   


class MeetingCreateView(LoginRequiredMixin, CreateView):
    model = Meeting  
    form_class = MeetingCreateForm
    success_url = reverse_lazy('soc_events:meeting-admin')
    template_name = 'soc_events/meeting_form.html'
    

class MeetingUpdateView(LoginRequiredMixin, UpdateView):
    model = Meeting
    form_class = MeetingCreateForm
    success_url = reverse_lazy('soc_events:meeting-admin')

class MeetingDeleteView(LoginRequiredMixin, DeleteView):
    model = Meeting
    success_url = reverse_lazy('soc_events:meeting-admin')


class MeetingAttendanceListView(MeetingAdminDetailView,ListView):
    model = MeetingAttendance 
    context_object_name = 'register'
    template_name = 'soc_events/meeting_attendance.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super(MeetingAttendanceListView, self).get_context_data(*args,**kwargs)
        context['absent'] = MeetingAttendance.objects.filter(is_present='False').count()
        context['present'] = MeetingAttendance.objects.filter(is_present='True').count()
        return context
        
# Funerals views

class FuneralList(LoginRequiredMixin, ListView):
    model = Funeral
    context_object_name = 'funerals'
    template_name = 'soc_events/funerals.html'   
    
class FuneralDetailView(LoginRequiredMixin, DetailView):
    model = Funeral
    context_object_name = 'funeral'
    template_name = 'soc_events/funeral_detail.html'
    
class FuneralAdminView(LoginRequiredMixin, ListView):
    model = Funeral
    context_object_name = 'funerals'
    template_name = 'soc_events/funeral_admin.html'
    
    
class FuneralAdminDetailView(LoginRequiredMixin, DetailView):
    model = Funeral
    context_object_name = 'funeral'
    template_name = 'soc_events/funeral_admin_detail.html'
    
    
class FuneralCreateView(LoginRequiredMixin,CreateView):
    model = Funeral
    form_class = FuneralCreateForm
    success_url = reverse_lazy('soc_events:funeral-admin')
    template_name = 'soc_events/funeral_form.html'

class FuneralUpdateView(LoginRequiredMixin,UpdateView):
    model = Funeral
    form_class = FuneralCreateForm
    success_url = reverse_lazy('soc_events:funeral-admin')
    template_name = 'soc_events/funeral_update.html'
    
class FuneralDeleteView(LoginRequiredMixin,DeleteView):
    model = Funeral
    success_url = reverse_lazy('soc_events:funeral-admin')
    
# Meetings attendances

def create_meeting_attendance(request, pk): 
    meeting = Meeting.objects.get(pk=pk)
    formset = MeetingAttendanceFormset(request.POST or None)
    if request.method == "POST":
        if formset.is_valid():
            formset.instance = meeting
            formset.save()
            return redirect ('soc_events:meeting', pk=meeting.id)
        
    context = {
        'formset': formset, 
        'meeting': meeting,  
    }     
    return render(request, 'soc_events/meeting_register.html', context )

# Funeral Attendances
def create_funeral_attendance(request, pk): 
    funeral = Funeral.objects.get(pk=pk)
    formset = FuneralAttendanceFormset(request.POST or None)
    if request.method == "POST":
        if formset.is_valid():
            formset.instance = funeral
            formset.save()
            return redirect ('soc_events:funeral', pk=funeral.id)
        
    context = {
        'formset': formset,   
        'funeral': funeral,  
    }     
    return render(request, 'soc_events/funeral_register.html', context )

# class MeetingAttendanceUpdateView(LoginRequiredMixin,UpdateView):
#     model = MeetingAttendance
#     form_class = MeetingAttendanceCreateForm
#     success_url = reverse_lazy('soc_events:meetings')
#     template_name = 'soc_events/meeting_attendance_update.html'


# class FuneralAttendanceUpdateView(LoginRequiredMixin,UpdateView):
#     model = FuneralAttendance
#     form_class = FuneralAttendanceCreateForm
#     template_name = 'soc_events/funeral_attendance_update.html'
#     success_url = reverse_lazy('soc_events:funeral-admin')
