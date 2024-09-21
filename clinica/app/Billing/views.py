from django.shortcuts import render
from rest_framework import viewsets
from .models import Billing
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BillingsSerializers

class BillingsViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingsSerializers
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,  
        filters.OrderingFilter,
    ]
    
    filterset_fields = ('__all__')
    search_fields = ('idPatient__firstName', 'idMedicalRecords__description', 'date','paymentStatus')
    ordering_fields = ('__all__')