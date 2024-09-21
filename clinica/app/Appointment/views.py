from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AppointmentsSerializers

class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentsSerializers
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,  
        filters.OrderingFilter,
    ]
    
    filterset_fields = ('__all__')
    search_fields = ('idPatient__firstName', 'idEmployee__firstName', 'datetime','status')
    ordering_fields = ('__all__')