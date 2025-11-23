from django.contrib import admin
from .models import TermsAndConditions, PrivacyPolicy, ContactDetails, Counter

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

@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'email', 'phone', 'updated_at']
    ordering = ['-updated_at']
    
    def has_add_permission(self, request):
        return not ContactDetails.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'map', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

