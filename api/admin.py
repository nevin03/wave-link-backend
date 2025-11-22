from django.contrib import admin
from .models import TermsAndConditions, PrivacyPolicy

@admin.register(TermsAndConditions)
class TermsAdmin(admin.ModelAdmin):
    list_display = ['id', 'updated_at']
    ordering = ['-updated_at']

@admin.register(PrivacyPolicy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['id', 'updated_at']
    ordering = ['-updated_at']
