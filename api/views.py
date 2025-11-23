from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import TermsAndConditions, PrivacyPolicy, ContactDetails, Counter
from .serializers import TermsSerializer, PrivacySerializer, ContactDetailsSerializer, CounterSerializer

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

class CounterPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CounterListView(generics.ListAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    pagination_class = CounterPagination

