from django.db import models
from clinica.app.Employees.models import Employees
from clinica.app.Patients.models import Patients

class Appointment(models.Model):
    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        
    idPatient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=False)
    idEmployee = models.ForeignKey(Employees, on_delete=models.CASCADE, blank=False)
    datetime = models.DateTimeField(blank=False, null= False)
    reason = models.CharField('Reason', max_length=100, blank = True)
    status = models.BooleanField('Status',default=False)
    
    
    def __str__(self):
        return f'{self.datetime} - {self.idPatient} - {self.idEmployee} - {self.reason}'