from django.contrib import admin
from .models import MemberAccount, Fine, Topup

class TopupsInline (admin.TabularInline):
    model = Topup
    
class FinesInline (admin.TabularInline):
    model = Fine

class MemberAccountAdmin(admin.ModelAdmin):
    list_display = ['name','date', 'balance_brought_forward',
                    'premiums','fines','topups', 'total_debits',
                    'cash_deposits','adjustments','total_receipts',
                    'net_movement','total_outstanding']
    
    list_editable = ('date','balance_brought_forward',
                    'adjustments')

    list_display_links = ('name',)
    list_filter = ('name',)
    inlines = [FinesInline, TopupsInline]
    list_per_page =15
    

class FineAdmin(admin.ModelAdmin):
    list_display = ['member','fine_type','amount','description']
    list_filter = ('member','fine_type')
    list_display_links = ('member',)
    list_per_page = 10
    
class TopupAdmin(admin.ModelAdmin):
    list_display = ['member', 'topup_type',
                    'amount','description']
    list_display_links = ('member','topup_type')
    list_filter = ('member',)
    list_per_page = 10

# Register your models here.
admin.site.register(MemberAccount, MemberAccountAdmin)
admin.site.register(Fine, FineAdmin)
admin.site.register(Topup, TopupAdmin)