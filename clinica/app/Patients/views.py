from django.shortcuts import render
from rest_framework import viewsets
from .models import Patients
from rest_framework import filters
from django_filters.rest_framework import   DjangoFilterBackend
from .serializers import *

class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializers
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    
    filterset_fields = ("__all__")
    search_fields = ('firstName', 'lastName', 'email', 'username')
    ordering_fields = ('__all__')