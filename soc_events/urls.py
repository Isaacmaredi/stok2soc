from django.urls import path

from soc_events.models import Funeral
from . import views

app_name = 'soc_events'

urlpatterns = [
    path('meeting_list/',views.MeetingList.as_view(), name='meetings'),
    path('meeting_admin/',views.MeetingAdminView.as_view(), name='meeting-admin'),
    path('meeting_detail/<int:pk>/',views.MeetingDetail.as_view(), name='meeting'),
    path('meeting_admin/<int:pk>/',views.MeetingAdminDetailView.as_view(), 
            name='meeting-admin-detail'
            ),
    path('meeting_create/',views.MeetingCreateView.as_view(), 
            name='meeting-add'
            ),
    path('meeting_update/<int:pk>/',views.MeetingUpdateView.as_view(), 
            name='meeting-update'
            ),
    path('meeting_delete/<int:pk>/',views.MeetingDeleteView.as_view(), 
            name='meeting-delete'
            ),
    path('meeting_attendance/<int:pk>/meeting_attendance',views.create_meeting_attendance, 
            name='meeting-attendance'
            ),
    # path('<int:pk>/meeting_attendance_update',views.MeetingAttendanceUpdateView.as_view(), name='meeting-attendance-update'),
    # path('meeting_update/',views.MeetingUpdate.as_view(), name='meeting_update'),   
    # path('attendance/<int:pk>/',views.MeetingAttendanceListView.as_view(), name='attendance'),
    path('funeral_list/',views.FuneralList.as_view(), name='funerals'),
    path('funeral_detail/<int:pk>', views.FuneralDetailView.as_view(), name='funeral'),
    path('funeral_admin/',views.FuneralAdminView.as_view(), name='funeral-admin'),
    path('funeral_admin/<int:pk>/',views.FuneralAdminDetailView.as_view(), 
            name='funeral-admin-detail'
            ),
    path('funeral_create/',views.FuneralCreateView.as_view(), name='funeral-add'),
    path('funeral_update/<int:pk>/update', views.FuneralUpdateView.as_view(), 
            name='funeral-update'
            ),
    path('funeral_delete/<int:pk>/delete',views.FuneralDeleteView.as_view(), 
            name='funeral-delete'
            ),
    path('funeral_attendance/<int:pk>/funeral_attendance',views.create_funeral_attendance, 
            name='funeral-attendance'
            ), 
    # path('funeral-attendance/<int:pk>/funeral_attendance_update',views.FuneralAttendanceUpdateView.as_view(), 
    #         name='funeral-attendance-update'
    #         ),
]