from django.shortcuts import render, redirect  

from django.views.generic import ListView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MemberAccount, Fine, Topup, Cashflow


class MemberAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'soc_finance/member_accounts.html'
    
class MemberAccountAdminView(LoginRequiredMixin, TemplateView):
    template_name = 'soc_finance/member_accounts_admin.html'
    

class CashflowView(LoginRequiredMixin, TemplateView):
    template_name = 'soc_finance/cashflow.html'
    
class CashflowAdminView(LoginRequiredMixin, TemplateView):
    template_name = 'soc_finance/cashflow_admin.html'

