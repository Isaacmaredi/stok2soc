from multiprocessing import context
from re import T
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from soc_members.models import Member, Beneficiary
from django.db.models import Count
# Create your views here.

# class MainDashView(LoginRequiredMixin, View):
#     model = Member
#     template_name = 'soc_dash/index.html'
#     context_object_name = 'members'
    
def main_dash(request):
    member_count = Member.objects.all().count()
    beneficiary_count = Beneficiary.objects.all().count()
    active_members = Member.objects.filter(status ='Active').count()
    active_beneficiaries= Beneficiary.objects.filter(beneficiary_status='Active').count()
    # status_count = Member.objects.values('status').order_by('status').annotate(count=Count('status'))
    print('Active Bens: ', active_beneficiaries)
    
    # status_members = Member.objects.order_by().values_list('status').distinct()
    # print('Position 0 is: ', status_count[0], '', 'and Position 1 is', status_count[1])
    
    
    status_labels = ['Active', 'Deceased', 'Suspended', 'Terminated']
    
    qs = Member.objects.values()
    status_count = []
    active = 0
    deceased = 0
    suspended = 0
    terminated = 0
    
    for i in qs:
        if 'Active' in i.values():
            active += 1 
        elif 'Deceased' in i.values():
            deceased+= 1
        elif 'Suspended' in i.values():
            suspended += 1
        elif 'Terminated' in i.values():
            terminated += 1
    status_count.extend([active, deceased, suspended, terminated])
    print()
    print('Status Labels:',status_labels)
    print()
    print('Status Count: ', status_count)

    
    
    # for i in len(status_count):
        
    
    # for key, value in status_count:
    #     status_name.append(key.item)
    #     status_name_count.append(value.item)
    
    context = {
        'member_count': member_count, 
        'active_members':active_members,
        'beneficiary_count':beneficiary_count,
        'active_beneficiaries': active_beneficiaries,
        'status_count': status_count,
        'status_labels': status_labels
    }
    return render(request, 'soc_dash/index.html', context)