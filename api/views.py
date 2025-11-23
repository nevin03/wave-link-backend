from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TermsAndConditions, PrivacyPolicy, ContactDetails
from .serializers import TermsSerializer, PrivacySerializer, ContactDetailsSerializer

class TermsView(APIView):
    def get(self, request):
        obj = TermsAndConditions.objects.last()
        if obj:
            return Response(TermsSerializer(obj).data)
        return Response({"content": ""})  # fallback if empty

class PrivacyView(APIView):
    def get(self, request):
        obj = PrivacyPolicy.objects.last()
        if obj:
            return Response(PrivacySerializer(obj).data)
        return Response({"content": ""})

class ContactDetailsView(APIView):
    def get(self, request):
        obj = ContactDetails.objects.last()
        if obj:
            return Response(ContactDetailsSerializer(obj).data)
        return Response({"name": "", "address": "", "email": "", "phone": ""})
