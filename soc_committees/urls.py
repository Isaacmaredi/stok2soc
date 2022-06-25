from django.urls import path

from .views import * 

app_name = 'soc_committees'

urlpatterns = [
    path('committees/',CommitteeListView.as_view(), name = 'committees'),
    path('committees/<int:pk>/',CommitteeDetailView.as_view(), name = 'committee-detail'),
    path('committees/add',CommitteeCreateView.as_view(), name = 'committee-add'),
    path('committees/<int:pk>/update',CommitteeUpdateView.as_view(), name = 'committee-update'),
    path('committees/<int:pk>/delete',CommitteeDeleteView.as_view(), name = 'committee-delete'),
    path('committees_admin/',CommitteeAdminView.as_view(), name = 'committee-admin'),
    path('committee/<int:pk>/',CommitteeAdminDetailView.as_view(), name='committee-admin-detail'),
    # Committee Incumbents
    path('committees/<int:pk>/create_incumbents/', create_incumbents, name='incumbent-add'),
    path('committees/<int:pk>/incumbent_delete/', IncumbentDeleteView.as_view(), name='incumbent-delete')  
]  
