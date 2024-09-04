from django.shortcuts import render
from rest_framework import viewsets
from .models import * 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class medicineInventoryViewset(viewsets.ModelViewSet):
    queryset = MedicineInventory.objects.all()
    serializer_class = medicineInventorySerializers
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')