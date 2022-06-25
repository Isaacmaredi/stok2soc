from pydoc import classname
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView,
                                DetailView,
                                UpdateView,
                                CreateView,
                                DeleteView)

from .models import Committee, Incumbent
from .forms import *

# Create your views here.

class CommitteeListView(LoginRequiredMixin,ListView):
    context_object_name = "committees"
    model = Committee
    print('committees')
    template_name = 'soc_committees/committee_list.html'

class CommitteeDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'committee'
    model = Committee
    template_name = 'soc_committees/committee_detail.html'
    

class CommitteeCreateView(LoginRequiredMixin, CreateView):
    model = Committee
    form_class = CommitteeCreateForm
    success_url = reverse_lazy('soc_committees:committee-admin')


class CommitteeUpdateView(LoginRequiredMixin, UpdateView):
    model = Committee
    form_class = CommitteeCreateForm
    template_name = 'soc_committees/committee_update.html'
    success_url = reverse_lazy('soc_committees:committee-admin')

class CommitteeDeleteView(LoginRequiredMixin, DeleteView):
    model = Committee
    success_url = reverse_lazy('soc_committees:committee-admin')

class CommitteeAdminView(LoginRequiredMixin,ListView):
    model = Committee
    template_name = 'soc_committees/committee_admin.html'
    context_object_name = "committee_list"
    
    def get_context_data(self, *args, **kwargs):
        context = super(CommitteeAdminView, self).get_context_data(*args, **kwargs)
        context['total'] = Committee.objects.all().count()
        return context

class CommitteeAdminDetailView(LoginRequiredMixin, DetailView):
    model = Committee
    context_object_name = 'committee'
    template_name = 'soc_committees/committee_detail_admin.html'
    

class IncumbentCreateView(LoginRequiredMixin, CreateView):
    model = Incumbent
    form_class = None
    success_url = reverse_lazy('soc_committees:committees')
    fields = ['committee','member','portfolio']

def create_incumbents(request, pk): 
    committee = Committee.objects.get(pk=pk)
    formset = IncumbentFormset(request.POST or None)
    if request.method == "POST":
        if formset.is_valid():
            formset.instance = committee
            formset.save()
            return redirect ('soc_committees:committee-admin')
    context = {
        'formset': formset,
        'committee': committee,     
        }
    
    return render(request, 'soc_committees/incumbent_form.html', context)  
    
class IncumbentListView(LoginRequiredMixin, ListView):
    model = Incumbent
    template_name = 'soc_committees/incumbent_list.html'
    

class IncumbentDeleteView(LoginRequiredMixin, DeleteView):
    model = Incumbent
    success_url = reverse_lazy('soc_committees:committee-admin')
    
