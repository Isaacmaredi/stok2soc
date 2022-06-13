from django.urls import path

from .import views

app_name = 'soc_members'

urlpatterns = [
    path('member_add/', views.MemberCreateView.as_view(), name='member-add'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('members_admin', views.MemberAdminView.as_view(), name='members-admin'),
    # path('members/', views.MemberSearchlistView.as_view(), name='members-search'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member'),
    path('my_profile_detail/<int:pk>/', views.MyProfileDetailView.as_view(), name='my-profile-detail'),
    path('member/<int:pk>/edit/', views.MemberUpdateView.as_view(), name='member-edit'),
    path('member/<int:pk>/beneficiary_edit', views.BeneficiaryUpdateView.as_view(),name='beneficiary_edit'),
    path('member/<int:pk>/beneficiary_edit/', views.manage_beneficiaries, name='beneficiary_edit'),
    path('members/beneficiaries/', views.BeneficiaryListView.as_view(), name='beneficiaries'),   
]