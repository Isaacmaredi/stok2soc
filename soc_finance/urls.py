from django.urls import path

from . import views

app_name = 'soc_finance'

urlpatterns = [
    path('finances/member_accounts/', views.MemberAccountView.as_view(), name='member-accounts'), 
    path('finances/member_accounts_admin/', views.MemberAccountAdminView.as_view(), name='member-accounts-admin'), 
    path('finances/cashflow/', views.CashflowView.as_view(), name='cashflow'), 
    path('finances/cashflow_admin/', views.CashflowAdminView.as_view(), name='cashflow-admin'), 
]