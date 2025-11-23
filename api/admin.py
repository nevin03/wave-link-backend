from django.contrib import admin
from .models import TermsAndConditions, PrivacyPolicy

@admin.register(TermsAndConditions)
class TermsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'updated_at']
    ordering = ['-updated_at']
    
    def has_add_permission(self, request):
        return not TermsAndConditions.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(PrivacyPolicy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'updated_at']
    ordering = ['-updated_at']
    
    def has_add_permission(self, request):
        return not PrivacyPolicy.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
