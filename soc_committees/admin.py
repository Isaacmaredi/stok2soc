from django.contrib import admin

from .models import Committee, Incumbent

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['name','shortname','term_starts','term_ends']
    list_filter = ('name',)

admin.site.register(Committee, CommitteeAdmin)

class IncumbentAdmin(admin.ModelAdmin):
    list_display =['committee','member','portfolio']
    list_filter = ('committee',)
    list_per_page = 15
    
admin.site.register(Incumbent, IncumbentAdmin)
