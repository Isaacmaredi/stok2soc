from django.contrib import admin

from .models import Beneficiary

# Register your models here.

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ['member','full_name','beneficiary_type',
                    'beneficiary_status','is_paid','paid_date',
                    ]
    list_editable = ('beneficiary_status','is_paid','paid_date')
    list_display_links = ('full_name',)
    list_filter = ('beneficiary_type', 'beneficiary_status','member')
    search_fields = ('member',)
    list_per_page = 20
    
admin.site.register(Beneficiary, BeneficiaryAdmin)
