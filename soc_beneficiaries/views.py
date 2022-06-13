from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import Beneficiary

from .forms import BeneficiaryCreateForm

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BeneficiaryListView(ListView):
    model = Beneficiary
    context_object_name = 'beneficiaries'
    # success_url = reverse ('soc_beneficiaries:beneficiaries')
    template_name = 'soc_beneficiaries/beneficiaries.html'
    
class BeneficiaryDetailView(DetailView):
    model = Beneficiary
    context_object_name = 'beneficiary'
    template_name = 'soc_beneficiary:beneficiary'
    
class BeneficiaryCreateView(CreateView):
    model = Beneficiary 
    form_class = BeneficiaryCreateForm
    success_url = reverse_lazy ('soc_beneficiaries:beneficiaries')
