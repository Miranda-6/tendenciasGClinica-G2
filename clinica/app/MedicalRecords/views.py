from django.shortcuts import render
from rest_framework import viewsets
from .models import MedicalRecords
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MedicalRecordSerializers

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecords.objects.all()
    serializer_class = MedicalRecordSerializers
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,  
        filters.OrderingFilter,
    ]
    
    filterset_fields = ('__all__')
    search_fields = ('idPatient__firstName', 'idEmployees__firstName', 'idMedicineInventory__nameMedicine')
    ordering_fields = ('__all__')