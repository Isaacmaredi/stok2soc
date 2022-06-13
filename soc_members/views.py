from re import M
from django.shortcuts import render
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
from .forms import MemberCreateForm,  BeneficiaryFormset, MemberSearchForm
  


class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberCreateForm 
    template_name = 'soc_members/member_form1.html'
    
class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberCreateForm 
    template_name = 'soc_members/member_form1.html'
    
    
class MemberListView (LoginRequiredMixin, ListView):
    model = Member
    context_object_name ='members'
    form_class = MemberSearchForm
    template_name = 'soc_members/member_list.html'
    paginate_by = 8
    # queryset = Member.objects.filter(status__icontains='act')


    def get_queryset(self):  
        member_query = self.request.GET.get('q', default="") 
        member_search =  Member.objects.filter(full_name__icontains=member_query)
        return member_search
    
    # def get_queryset(self):
    #     status_query = self.request.GET.get('s', default="")
    #     status_search = Member.objects.filter(status__iexact=status_query)
    #     return status_search
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(MemberListView, self).get_context_data(*args, **kwargs)
        context['actives'] = Member.objects.filter(status='Active').count() 
        context['deceased'] = Member.objects.filter(status='Deceased').count()
        context['suspended'] = Member.objects.filter(status='Suspended').count()
        context['terminated'] = Member.objects.filter(status='Terminated').count()
        context['total'] = Member.objects.all().count()
        context['member_search'] = 'member_search'
        # context['status_search'] = 'status_search'
        return context 

class MemberAdminView(LoginRequiredMixin, ListView):
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
    
    def get_queryset(self):
        query = self.request.GET.get('q', default="") 
        
        status_search = Member.objects.filter(
            Q(status__iexact=query) 
        )
        return status_search 
    
    def get_context_data(self, *args, **kwargs):
        context = super(MemberAdminView, self).get_context_data(*args, **kwargs)
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
    
    def test_func(self):
        member = self.get_object()
        if self.request.user.id == member.id:
            print('User ID: ',self.request.user.id, '-- Member ID: ', member.id)
            return True
        return False
    
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

    
def manage_beneficiaries(request, pk):
    progress = 60
    member = Member.objects.get(pk=pk)
    if request.method == "POST":
        formset = BeneficiaryFormset(request.POST, request.FILES, instance=member)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(member.get_absolute_url())
    else:
        formset = BeneficiaryFormset(instance=member)
        
        context = {
            'formset': formset,
            'member': member,  
            'progress': progress,   
        }
        
    return render(request, 'soc_members/member_form.html', context )


# class BeneficiaryUpdateView(UpdateView):
#     model = Member
#     fields = ['user']
#     success_url = reverse_lazy('soc_members:members')

#     def get_context_data(self, **kwargs):
#         data = super(BeneficiaryUpdateView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['beneficiaries'] = BeneficiaryFormset(self.request.POST)
#         else:
#             data['beneficiaries'] = BeneficiaryFormset()
#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         beneficiaries = context['beneficiaries']
#         with transaction.atomic():
#             self.object = form.save()

#             if beneficiaries.is_valid():
#                 beneficiaries.instance = self.object
#                 beneficiaries.save()
#         return super(BeneficiaryUpdateView, self).form_valid(form)

class BeneficiaryUpdateView(SingleObjectMixin, FormView):
    model = Member
    fields = ['user', 'middlename','mobile_phone',]
    template_name = 'soc_members/beneficiary_edit.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Member.objects.all())
        super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Member.objects.all())
        super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return BeneficiaryFormset(**self.get_form_kwargs(), instance= self.object)
    
    def form_valid(self, form):
        form.save()
    
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Beneficiaries have been added'
        )
        
        return HttpResponseRedirect(reverse('soc_members:member', kwargs={'pk': self.object.pk}))
    
    # def get_success_url(self):
    #     return reverse('soc_members:member', kwargs={'pk': self.object.pk})
        
    #     data = super(BeneficiaryUpdateView, self).get_context_data(**kwargs)
        
    #     if self.request.POST:
    #         data['beneficiaries'] = BeneficiaryInlineFormset(self.object, instance = self.object)
    #     else:
    #         data['beneficiaries'] = BeneficiaryInlineFormset()  
    #     return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     beneficiaries = context['beneficiaries']
    #     with transaction.atomic():
    #         self.object = form.save()

    #         if beneficiaries.is_valid():
    #             beneficiaries.instance = self.object
    #             beneficiaries.save()
    #     return super(BeneficiaryUpdateView, self).form_valid(form)
    

        
    

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     beneficiaries = context['beneficiaries']
    #     with transaction.atomic():
    #         self.object = form.save()

    #         if beneficiaries.is_valid():
    #             beneficiaries.instance = self.object
    #             beneficiaries.save()
    #     return super(BeneficiaryUpdateView, self).form_valid(form)
    
    
    # model = Member
    # template_name = 'soc_members/beneficiary_edit.html'
    # # form_class = BeneficiaryCreateForm
    
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object(queryset=Member.objects.all())
    #     super().get(request, *args, **kwargs)   
        
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object(queryset=Member.objects.all())
    #     super().get(request, *args, **kwargs)  
        
    # def get_form(self, form_class=None):
    #     return BeneficiaryInlineFormset(**self.get_form_kwargs(), instance= self.object)
        
    # def form_valid(self, form):
    #     form.save()
        
    #     messages.add_message(
    #         self.request,
    #         messages.SUCCESS,
    #         'Beneficiaries have been added'
    #     )
        
    #     return HttpResponseRedirect(self.get_success_url())
    
    # def get_success_url(self):
    #     return reverse('soc_members:members')
    

    
    
