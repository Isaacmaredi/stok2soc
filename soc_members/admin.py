from django.contrib import admin
from .models import Member, Beneficiary

class BeneficiaryInline(admin.TabularInline):
    model = Beneficiary

class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date','mobile_phone',
                    'status','status_date']
    list_display_links = ('user',)
    list_filter = ('status',)
    search_fields = ('user__username',)
    inlines =[BeneficiaryInline]
    list_per_page = 10


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'beneficiary_type','proxy',
                    'birth_date', 'beneficiary_status',
                    'is_paid','paid_date']
    list_display_links = ('full_name',)
    list_filter = ('beneficiary_status','is_paid', 'beneficiary_type','member',)
    search_fields = ('full_name',)
    list_per_page = 15


admin.site.register(Member, MemberAdmin)

admin.site.register(Beneficiary, BeneficiaryAdmin)
