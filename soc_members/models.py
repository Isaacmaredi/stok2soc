import re
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
STATUS_CHOICES =[
    ('Active','Active'),
    ('Inactive','Inactive'),
    ('Deceased','Deceased'),
    ('Suspended','Suspended'),
    ('Terminated','Terminated'),
]

beneficiary_type = [
    ("Spouse","Spouse"),
    ("Child","Child"),
    ("Father","Father"),
    ("Mother","Mother"),
    ("Father-in-Law","Father-in-Law"),
    ("Mother-in-Law","Mother-in-Law"),
    ("Parent Proxy","Parent Proxy"),
    ('Other','Other'),
]    

beneficiary_status = [
    ('Active','Active'),
    ('Deceased', 'Deceased'),
    ('Inactive', 'Inactive'), 
]

PROXY_CHOICES=[
    ('Father','Father'),
    ('Mother','Mother'),
    ('Father-in_Law','Father-in-Law'),
    ('Mother-in-Law','Mother-in-Law'),
    ('Other','Other'),
]


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    middlename = models.CharField(max_length=100, blank = True,null=True)
    full_name = models.CharField(max_length=250,blank=True, null=True)
    birth_date = models.DateField(auto_now=False, null=True, blank=False)
    mobile_phone = models.CharField(max_length=20)
    status = models.CharField(choices = STATUS_CHOICES, max_length=15, default='Active')
    status_date = models.DateField(auto_now=False, blank=True,null=True)
    cover_lapse_date = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=200)
    photo = models.ImageField(default='static/img/default2.png', upload_to='member_photos/%Y')
    
    def __str__(self):
        if self.middlename:
            return f'{self.user.last_name} {self.user.first_name[0]}{self.middlename[0]}'
        else:
            return f'{self.user.last_name} {self.user.first_name[0]}'
    
    def save(self, *args, **kwargs):
        if self.middlename:
            self.full_name = self.user.first_name + ' ' + self.middlename + ' ' + self.user.last_name
        else:
            self.full_name = self.user.first_name + ' ' + self.user.last_name
        return super(Member, self).save(*args, **kwargs)
    
    
    def get_absolute_url(self):
        return reverse('soc_members:member', kwargs= {'pk':self.pk})
    
    class Meta:
        ordering=('user_id',)
    
class Beneficiary(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE, 
                            related_name='beneficiaries')
    full_name = models.CharField(max_length=400)
    beneficiary_type = models.CharField(verbose_name="Beneficiary Type",
                                        max_length=100, 
                                        choices=beneficiary_type,
                                        default="Spouse")
    proxy = models.CharField(max_length=100,choices=PROXY_CHOICES, null=True,blank=True)
    birth_date = models.DateField(verbose_name="Date of Birth")
    beneficiary_status = models.CharField( verbose_name="Beneficiary Status",
                                        max_length=100,
                                        choices=beneficiary_status, 
                                        default="Active")
    is_paid = models.BooleanField(verbose_name= "Paid-up", default=False)
    paid_date = models.DateField(verbose_name='Paid-up Date', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Beneficiaries'
        ordering = ('id',)
    
    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('soc_members:member', kwargs= {'pk':self.member_pk})
