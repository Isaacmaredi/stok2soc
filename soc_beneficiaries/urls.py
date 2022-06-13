from django.urls import path

from .views import BeneficiaryListView, BeneficiaryCreateView, BeneficiaryDetailView

app_name = 'soc_beneficiaries'

urlpatterns = [
    path('beneficiary-add/', BeneficiaryCreateView.as_view(), name='beneficiary-add'),
    path('beneficiaries/', BeneficiaryListView.as_view(), name='beneficiaries'),
    path('beneficiary/<int:pk>', BeneficiaryDetailView.as_view(), name='beneficiary'),
]