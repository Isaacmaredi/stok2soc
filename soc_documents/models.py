from pickle import MEMOIZE
from django.db import models
from soc_events.models import Meeting
from soc_members.models import Member

class Minutes(models.Model):
    title = models.OneToOneField(Meeting, on_delete=models.DO_NOTHING, related_name='meeting')
    date = models.DateField(auto_now_add=True)
    doc_file = models.FileField(upload_to='minutes/%Y/%F')
    uploaded_by = models.CharField(max_length= 200, blank=True, null=True)
    def __str__(self):
        return f'Minutes - {self.title}'
    
    class Meta:
        verbose_name_plural = 'Minutes'
    
    




    