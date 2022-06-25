from django.urls import path
from . import views

app_name = 'soc_documents'

urlpatterns =[
    # Minutes urls
    path('documents/minutes/', views.MinutesListView.as_view(), name='minutes_list'),
    # path('minutes_list/',views.minutes_list, name='minutes_list'),
    path('minutes/minutes_admin/', views.MinutesAdminListView.as_view(), name='minutes-admin'),
    path('minutes/<int:pk>/update/', views.MinutesUpdateView.as_view(), name='minutes-update'),
    path('minutes/<int:pk>/delete/', views.MinutesDeleteView.as_view(), name='minutes-delete'),
    path('upload_minutes/',views.upload_minutes, name='upload_minutes'),
    
    # Policy URLs
    path('documents/policy/', views.PolicyListView.as_view(), name='policy_list'),
    # path('minutes_list/',views.minutes_list, name='minutes_list'),
    path('policy/policy_admin/', views.PolicyAdminListView.as_view(), name='policy-admin'),
    path('policy/<int:pk>/update/', views.PolicyUpdateView.as_view(), name='policy-update'),
    path('policy/<int:pk>/delete/', views.PolicyDeleteView.as_view(), name='policy-delete'),
    path('upload_policy/',views.upload_policy, name='upload_policy'),
]