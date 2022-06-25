import re
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from soc_members.models import Member, Beneficiary
from datetime import datetime, date
from django.urls import  reverse 


class Meeting(models.Model):
    date = models.DateField()
    
    MEETINGS = [
        ('Quartely Meeting','Quartely Meeting'),
        ('Special Meeting','Special Meeting'),
        ('Year-end Function','Year-end Function'),
        ('Extraordinary Meeting','Extraordinary Meeting'),  
    ]
    meeting_type = models.CharField(max_length=200, choices=MEETINGS)
    host = models.ForeignKey(Member, null=True, blank=True, 
                            on_delete=models.DO_NOTHING, related_name="meetings")
    alt_venue = models.CharField(max_length=300,blank=True, null=True)
    
    def __str__(self):
        return f'{self.meeting_type} held on {self.date}'
    
    class Meta:
        ordering = ('-date',)

class Funeral(models.Model):
    date = models.DateField()
    bereaved_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="bereaved")
    DECEASED_TYPE = [
        ('Member','Member') ,
        ('Beneficiary','Beneficiary'),
    ]
    deceased_type = models.CharField(max_length=100, choices=DECEASED_TYPE)
    deceased_member = models.OneToOneField(Member,on_delete=models.CASCADE, null=True, blank=True)
    deceased_beneficiary = models.OneToOneField(Beneficiary, on_delete=models.CASCADE, null=True,blank=True)
    # deceased_member = models.OneToOneField(Member, on_delete=models.CASCADE, null=True, blank=True)
    venue = models.CharField(max_length=200)
    
    def __str__(self):
        if self.deceased_type == "Member":
            deceased = self.deceased_member
        else:
            deceased = self.deceased_beneficiary
        
        return f'Funeral of {deceased} on {self.date}' 

class FuneralAttendance(models.Model):
    funeral = models.ForeignKey(Funeral, on_delete=models.CASCADE, related_name='funeral_attendances')
    member= models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member_funerals')
    is_present = models.BooleanField(default=True)
    ABSENCE_CHOICES = [
        ('Family Commitment','Family Commitment'),
        ('Ill-Health','Ill-Health'),
        ('Work Commitment','Work Commitment'),
        ('Funeral','Funeral'),
    ]
    absence_reason = models.CharField(choices=ABSENCE_CHOICES, max_length=300, null=True, blank=True)
    
    def __str__(self):
        return f'Funeral Attendance of {self.funeral}\' on {self.funeral.date}'
    
class MeetingAttendance(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='meeting_attendances')
    member= models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member_meetings')
    is_present = models.BooleanField(default=True)
    ABSENCE_CHOICES = [
        ('Family Commitment','Family Commitment'),
        ('Ill-Health','Ill-Health'),
        ('Work Commitment','Work Commitment'),
        ('Funeral Attendance','Funeral Attendance'),
    ]
    absence_reason = models.CharField(choices=ABSENCE_CHOICES, max_length=300, null=True, blank=True)
    
    def __str__(self):
        return f'{self.meeting} Member: {self.member} - Present: {self.is_present}'