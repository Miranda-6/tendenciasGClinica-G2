from rest_framework import serializers
from .models import Employees
from django.contrib.auth.hashers import make_password
from django.contrib.auth import hashers


class EmployeesSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) #No permite leer la contraseña
        
    class Meta:
        model = Employees
        fields = ('__all__')
        
    
    """ def create(self, validated_data):
        #Cuando se crea el usuario, encriptamo la contraseña
        user = Employees.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']) #Encripta la contraseña
        )
        return user """
        
    def create (self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Employees.objects.create(**validated_data)