from rest_framework import serializers
from .models import MedicalRecords

class MedicalRecordSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = MedicalRecords
        fields = ('__all__')