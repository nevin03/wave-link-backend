from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TermsAndConditions, PrivacyPolicy
from .serializers import TermsSerializer, PrivacySerializer

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
