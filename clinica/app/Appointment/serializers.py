from rest_framework import serializers
from .models import Appointment
from ..Patients.models import Patients
from ..Employees.models import Employees


class AppointmentsSerializers(serializers.ModelSerializer):
    idEmployee = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all())
    idPatient = serializers.PrimaryKeyRelatedField(queryset=Patients.objects.all())
    
    class Meta:
        model = Appointment
        fields = ['id', 'idPatient', 'idEmployee', 'datetime', 'reason', 'status']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['idEmployee'] = {
            'id': instance.idEmployee.id,
            'name': instance.idEmployee.firstName,
            'lastName': instance.idEmployee.lastName,
            'email': instance.idEmployee.email,
        }
        representation['idPatient'] = {
            'id': instance.idPatient.id,
            'name': instance.idPatient.firstName,
            'lastname': instance.idPatient.lastName,
            'email': instance.idPatient.email,
        }
        return representation