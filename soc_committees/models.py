from re import M
from django.db import models
from soc_members.models import Member


COMMITTEE_CHOICES =[
    ('Executive Committee', 'Executive Committee'),
    ('Finance Committee','Finance Committee'),
    ('Constitutional Committee','Constitutional Committee'),
    ('Disciplinary Committee','Disciplinary Committee'),
    ('Events Committee','Events Committee'),
    ('Compassion Committee','Compassion Committee')
]

PORTFOLIO_CHOICES = [
    ('Chairperson','Chairperson'),
    ('Deputy Chairperson','Deputy Chairperson'),
    ('Secetary-General','Secretary-General'),
    ('Deputy Secretary-General', 'Deputy Secretary-General'),
    ('Treasurer-General', 'Treasurer-General'),
    ('Events Coordinator', 'Events Cordinator'),
    ('Member of EXCO', 'Member of Exco'),
    ('Convenor','Convenor'),
    ('Member','Member'),
    ('Ex Officio Member','Ex Officio Member'),
]

class Committee(models.Model):
    name = models.CharField(max_length=200,choices=COMMITTEE_CHOICES)
    SHORTNAMES = [
        ('EXCO','EXCO'),
        ('FINCOM','FINCOM'),
        ('CONCOM','CONCOM'),
        ('DC','DC'),
        ('COMPCOM','COMPCOM'),
        ('ECOM','ECOM'),
        ]
    shortname = models.CharField(max_length=100, choices=SHORTNAMES)
    term_starts = models.DateField()
    term_ends = models.DateField()
    
    class Meta:
        ordering =['id']

    def __str__(self):
        return self.name 
    

class Incumbent(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='incumbents')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    portfolio = models.CharField(max_length=200, choices=PORTFOLIO_CHOICES)
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return f'{self.member} - {self.portfolio} of {self.committee}'