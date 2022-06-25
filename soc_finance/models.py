from django.db import models

from soc_members.models import Member
from datetime import datetime, date
from django.utils import timezone
from decimal import Decimal
# Create your models here.


class MemberAccount(models.Model):
    name = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="profile")
    date = models.DateField(default=date.today)
    balance_brought_forward = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
    premiums = models.DecimalField(default=Decimal('150.00'), decimal_places=2, max_digits=10)
    fines =models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10, blank=True, null=True)
    topups =models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10, blank=True, null=True)
    total_debits = models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10, blank=True, null=True)
    cash_deposits = models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10, blank=True, null=True)
    adjustments = models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10, blank=True, null=True)
    total_receipts = models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10, blank=True, null=True)
    net_movement = models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10)
    total_outstanding = models.DecimalField(default=Decimal('0.00'), decimal_places=2, max_digits=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-date','id']
    
    def __str__(self):
        return f'Account Statement for {self.name.shortname}'
    
    def save(self, *args, **kwargs):
        self.total_debits = self.premiums + self.fines + self.topups
        self.total_receipts = self.cash_deposit + self.adjustments  
        self.net_movement = self.total_debits + self.total_receipts
        self.total_outstanding = self.balance_brought_forward + self.net_movement
        super(MemberAccount,self).save(*args, **kwargs)

TOPUP_CHOICES = [ 
    (None, 'Select top-up type'),
    ('funeral topup','Funeral Topup'),
    ('transport augmentation','Transport Augmentation'),
    ('special function','Special Function'),
]

class Topup(models.Model): 
    member = models.ForeignKey(MemberAccount, related_name="member_topups", on_delete=models.DO_NOTHING)
    amount = models.DecimalField(default= Decimal('0.0'), decimal_places=2, max_digits=10)
    topup_type = models.CharField(max_length=250, choices=TOPUP_CHOICES)
    description = models.CharField(max_length=350, blank=True, null=True)
    
    def __str__(self):
        return f'{self.member} Top-ups due as at {self.member.date}'
    
FINE_CHOICES = [
    (None, 'Select fine type'),
    ('meeting absence','Meeting Absence'),
    ('funeral absence','Funeral Absence'),
    ('late coming','Late Coming'),
    ('uniform','Uniform'),
    ('disciplinary action','Disciplinary Action'),
]

class Fine (models.Model):
    member = models.ForeignKey(MemberAccount,related_name='member_fines', on_delete=models.DO_NOTHING)
    fine_type = models.CharField(max_length=300, choices=FINE_CHOICES)
    amount = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
    description = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return f'{self.member} Fines due as at {self.member.date}'

# class Cashflow(models.Model):
#     date = models.DateField()
#     opening_bank_bal = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     expenses = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     income = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     closing_bank_bal = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)

#     def __str__(self):
#         return f'Cashflow Statement for: {date.month}'
        

# class Company(models.Model):
#     logo = models.ImageField(default='static/img/pml_logo5.png')
#     name = models.CharField(max_length=200)
#     trading_name = models.CharField(max_length=50, null=True, blank=True)
#     created = models.DateTimeField(auto_now_add = True)
#     purchase_date = models.DateField()
#     num_shares = models.IntegerField()
#     purchase_price = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     purchase_value =models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
    
    
#     class Meta:
#         verbose_name_plural = 'Companies'
    
#     def save(self, *args, **kwargs):
#         self.purchase_value = self.num_shares * self.purchase_price
#         super(Company, self).save(*args, **kwargs)
    
#     def __str__(self):
#         return self.name
    
# class Share(models.Model):
#     company = models.ForeignKey(Co, on_delete=models.CASCADE)
#     date = models.DateField(default=timezone.now)
#     current_share_price = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     current_value = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
    
#     def __str__(self):
#         return self.company.name
    
#     def save(self, *args, **kwargs):
#         self.current_value = self.company.no_shares * self.current_share_price
#         super(Share, self).save(*args, **kwargs)
    
# class Wealth(models.Model):
#     date = models.DateField()
#     closing_cash_balance = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     notice_acc_balance = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     monthly_shares_total = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
#     total_net_wealth = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=10)
    
#     class Meta:
#         verbose_name_plural = 'Wealth'
        
#     def __str__(self):
#         return f'Net Wealth as at {self.date}'
    
#     def save(self, *args, **kwargs):
#         self.total_net_wealth = self.closing_cash_balance + self.notice_acc_balance + self.monthly_shares_total
#         super(Wealth, self).save(*args, **kwargs)
