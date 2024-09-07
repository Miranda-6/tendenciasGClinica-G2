from django.db import models

class Patients(models.Model):
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        
    firstName = models.CharField('First Name', max_length=100)
    lastName = models.CharField('Last name', max_length=100)
    email = models.CharField('Email', max_length=100)
    phone = models.CharField('Phone', max_length=10)
    birthDate = models.DateField()
    address = models.CharField('Address', max_length=50)
    username = models.CharField('User', max_length=100)
    password = models.CharField('Psaasword', max_length=100)
    
    def __str__(self):
        return f'{self.firstName} - {self.email} - {self.phone}'