from django.contrib import admin
from .models import Checks, ScanProfiles

# Register your models here.
class ScanProfilesAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_base_profile', 'created_at']
    list_filter = ['is_base_profile']
    search_fields = ['name']
    filter_horizontal = ['checks']



admin.site.register(Checks)
admin.site.register(ScanProfiles, ScanProfilesAdmin)