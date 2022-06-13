from django.db import models
from soc_members.models import Member

# Create your models here.
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

class Beneficiary(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE, related_name='benes')
    full_name = models.CharField(max_length=256)
    beneficiary_type = models.CharField(verbose_name="Beneficiary Type" ,max_length=100,  choices=beneficiary_type, default="Spouse")
    proxy = models.CharField(max_length=100,choices=PROXY_CHOICES, null=True,blank=True)
    birth_date = models.DateField(verbose_name="Date of Birth")
    beneficiary_status = models.CharField( verbose_name="Beneficiary Status",max_length=100,choices=beneficiary_status, default="Active")
    is_paid = models.BooleanField(verbose_name= "Paid-up", default=False)
    paid_date = models.DateField(verbose_name='Paid-up Date', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Beneficiaries'
        ordering = ('id',)
    
    def __str__(self):
        return self.full_name
        
    