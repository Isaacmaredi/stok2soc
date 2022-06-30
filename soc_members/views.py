from distutils.log import Log
from multiprocessing import context
from re import M
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView, 
                                    DeleteView, 
                                    UpdateView,
                                    FormView,)
from django.views.generic.detail import SingleObjectMixin
from .models import Member, Beneficiary
from .forms import (MemberCreateForm,  
                    BeneficiaryFormset, 
                    BeneficiaryCreateForm, 
                    BeneficiaryAddForm,
                    MemberSearchForm)

class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberCreateForm 
    template_name = 'soc_members/member_form.html'
    
class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberCreateForm 
    template_name = 'soc_members/member_form.html'
    
    
class MemberListView (LoginRequiredMixin, ListView):
    model = Member
    context_object_name ='members'
    form_class = MemberSearchForm
    template_name = 'soc_members/member_list.html'
    paginate_by = 10

    def get_queryset(self):  
        member_query = self.request.GET.get('q', default="") 
        member_search =  Member.objects.filter(full_name__icontains=member_query)
        return member_search
    
    def get_context_data(self, *args, **kwargs):
        context = super(MemberListView, self).get_context_data(*args, **kwargs)
        context['active_count'] = Member.objects.filter(status='Active').count() 
        context['active'] = Member.objects.filter(status='Active') 
        context['deceased_count'] = Member.objects.filter(status='Deceased').count()
        context['suspended_count'] = Member.objects.filter(status='Suspended').count()
        context['terminated_count'] = Member.objects.filter(status='Terminated').count()
        context['total'] = Member.objects.all().count()
        context['member_search'] = 'member_search'
        # context['status_search'] = 'status_search'
        return context 

class MemberAdminListView(LoginRequiredMixin, ListView):
    model = Member
    context_object_name = 'members'
    template_name = 'soc_members/member_admin.html'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q', default="") 
        
        member_search = Member.objects.filter(
            Q(full_name__icontains=query) 
        )
        return member_search 
    
    def get_context_data(self, *args, **kwargs):
        context = super(MemberAdminListView, self).get_context_data(*args, **kwargs)
        context['actives'] = Member.objects.filter(status='Active').count() 
        context['deceased'] = Member.objects.filter(status='Deceased').count()
        context['suspended'] = Member.objects.filter(status='Suspended').count()
        context['terminated'] = Member.objects.filter(status='Terminated').count()
        context['total'] = Member.objects.all().count()
        context['member_search'] = 'member_search'
        context['status_search'] = 'status_search'
        return context   


class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    context_object_name = 'member'
    template_name= 'soc_members/member-detail.html'
    
class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('soc_members:members-admin')
    
class MemberAdminDetailView(LoginRequiredMixin, DetailView):
    model = Member
    context_object_name = 'member'
    template_name = 'soc_members/member_admin_detail.html'
    

    
class MyProfileDetailView(LoginRequiredMixin, UserPassesTestMixin , DetailView):
    model = Member 
    template_name = 'soc_members/my_profile_detail.html'
    context_object_name = 'my_profile'
    
    def get_object(self):
        try:
            self.member = Member.objects.get(pk=self.request.user.pk)
        except Member.DoesNotExist:
            self.member = None
        return self.member
    
    def test_func(self):
        member = self.get_object()
        if self.request.user.id == member.id:
            print('User ID: ',self.request.user.id, '-- Member ID: ', member.id)
            return True
        return False

    
class BeneficiaryListView(LoginRequiredMixin,ListView):
    model = Beneficiary
    context_object_name = 'beneficiaries'

    def get_context_data(self, *args, **kwargs):
        context = super(BeneficiaryListView, self).get_context_data(*args, **kwargs )
        context['actives'] = Beneficiary.objects.filter(beneficiary_status='Active')
        context['deceased'] = Beneficiary.objects.filter(beneficiary_status='Deceased')
        context['inactives'] = Beneficiary.objects.filter(beneficiary_status='Inactive')
        return context

class BeneficiaryCreateView(LoginRequiredMixin,CreateView):
    model = Beneficiary
    form_class = BeneficiaryAddForm
    success_url = reverse_lazy('soc_members:beneficiary-admin')
    

def create_beneficiaries(request, pk): 
    member = Member.objects.get(pk=pk)
    formset = BeneficiaryFormset(request.POST or None)
    if request.method == "POST":
        if formset.is_valid():
            formset.instance = member 
            formset.save()
            return redirect ('soc_members:member-admin-detail', pk=member.pk)
        
    context = {
        'formset': formset, 
        'member': member,    
    }     
    return render(request, 'soc_members/create_beneficiary.html', context )

class BeneficiaryAdminListView(LoginRequiredMixin,ListView):
    model = Beneficiary
    context_object_name = 'beneficiaries'
    template_name = 'soc_members/beneficiary_admin.html'
    paginate_by = 8
    
    def get_queryset(self):
        query = self.request.GET.get('q', default="") 
        
        beneficiary_search = Beneficiary.objects.filter(
            Q(full_name__icontains=query) 
        )
        return beneficiary_search 
    
    # def get_queryset(self):
    #     ben_query = self.request.GET.get('s', default="")
    #     beneficiary_status_search = Beneficiary.objects.filter(
    #         Q(beneficiary_status__icontains=ben_query))
    #     return beneficiary_status_search
    
    def get_context_data(self, *args, **kwargs):
        context = super(BeneficiaryAdminListView, self).get_context_data(*args, **kwargs)
        context['actives'] = Beneficiary.objects.filter(beneficiary_status='Active').count() 
        context['deceased'] = Beneficiary.objects.filter(beneficiary_status='Deceased').count()
        context['inactive'] = Beneficiary.objects.filter(beneficiary_status='Inactive').count()
        context['total'] = Beneficiary.objects.all().count()
        context['beneficiary_search'] = 'beneficiary_search'
        # context['beneficiary_status_search'] = 'beneficiary_status_search'
        return context  
 

class BeneficiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Beneficiary
    form_class = BeneficiaryCreateForm
    template_name = 'soc_members/beneficiary_update.html'
    success_url = reverse_lazy('soc_members:beneficiary-admin')
    
class BeneficiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Beneficiary
    success_url = reverse_lazy('soc_members:beneficiary-admin')
    
    
class MemberLoginAdminView(LoginRequiredMixin,ListView):
    model = Member
    context_object_name = 'members'
    order_by = ['-object.user.last_login']
    template_name = 'soc_members/member_logins.html'

    
    def get_context_data(self, *args, **kwargs):
        context = super(MemberLoginAdminView, self).get_context_data(*args, **kwargs)
        context['total'] = Member.objects.all().count()
        context['order'] = Member.objects.all().order_by('self.object__last_login')
        return context
        

    
    

    
    
