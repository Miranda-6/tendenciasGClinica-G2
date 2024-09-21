from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import hashers

# Create your models here.

class Employees(models.Model):
    
    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Employees"
        
    firstName = models.CharField('Nombres', max_length=100)
    lastName = models.CharField('Apellidos', max_length=100)
    email = models.EmailField('Correo electrónico', max_length=100)
    phone = models.CharField('Celular')
    birthdate = models.DateField('Fecha de nacimiento')
    address = models.CharField('Dirección', max_length=100)
    rol_options = (
        ("MED", "Medico(a)"),
        ("ENF", "Enfermero(a)"),
        ("ADM", "Administrativo"),
        ("LIM", "Limpieza"),
        ("REG", "Regente de farmacia"),
        ("FIS", "Fisioterapeuta"),
        ("OTR", "Otros")
    )
    
    rol = models.CharField('Cargo', max_length=50, blank=False, null=False, choices=rol_options, default='OTR')
    username = models.CharField('Nombre de usuario', max_length=50)
    password = models.CharField('Contraseña', max_length=100)
    
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Encripta la contraseña
        super(Employees, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.rol} - {self.username}"