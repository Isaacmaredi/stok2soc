from django.urls import path

from .import views

app_name = 'soc_members'

urlpatterns = [ 
    path('member_add/', views.MemberCreateView.as_view(), name='member-add'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('members_admin/', views.MemberAdminListView.as_view(), name='members-admin'),
    # path('members/', views.MemberSearchlistView.as_view(), name='members-search'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member'),
    path('members/<int:pk>/', views.MemberDeleteView.as_view(), name='member-delete'),
    path('my_profile_detail/<int:pk>/', views.MyProfileDetailView.as_view(), name='my-profile-detail'),
    path('member/<int:pk>/edit/', views.MemberUpdateView.as_view(), name='member-edit'),
    path('members_admin/<int:pk>/', views.MemberAdminDetailView.as_view(), name='member-admin-detail'),
    path('member_logins/',views.MemberLoginAdminView.as_view(), name='member-logins'),
    path('beneficiary_admin/', views.BeneficiaryAdminListView.as_view(), name='beneficiary-admin'), 
    path('beneficiary_admin/add/', views.BeneficiaryCreateView.as_view(), name='beneficiary-add'),
    path('beneficiary_admin/<int:pk>/update/', views.BeneficiaryUpdateView.as_view(),name='beneficiary-update'),
    path('beneficiary_admin/<int:pk>/delete/', views.BeneficiaryDeleteView.as_view(),name='beneficiary-delete'),
    path('member/<int:pk>/create_beneficiary/', views.create_beneficiaries, name='create-beneficiary'),
    path('members/beneficiaries/', views.BeneficiaryListView.as_view(), name='beneficiaries'),   
] 