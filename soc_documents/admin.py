from django.contrib import admin
from .models import Minutes


class MinutesAdmin(admin.ModelAdmin):
    fields = ('title', 'doc_file','uploaded_by')
    display_fields = ('title', 'doc_file', 'uploaded_by')
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Minutes, MinutesAdmin)
