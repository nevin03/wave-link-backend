from rest_framework import serializers
from .models import TermsAndConditions, PrivacyPolicy

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = ['content', 'updated_at']

class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['content', 'updated_at']
