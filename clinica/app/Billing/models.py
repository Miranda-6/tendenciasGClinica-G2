from django.db import models
from clinica.app.MedicalRecords.models import MedicalRecords
from clinica.app.Patients.models import Patients

class Billing(models.Model):
    class Meta:
        verbose_name = "Billing"
        verbose_name_plural = "Billings"
        
    idPatient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=False)
    idMedicalRecords = models.ForeignKey(MedicalRecords, on_delete=models.CASCADE, blank=False)
    date = models.DateField(auto_now_add=True)
    totalAmount = models.DecimalField(decimal_places=2)
    details = models.CharField('Details', max_length=100, blank = True)
    paymentStatus = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.date} - {self.idPatient} - {self.idMedicalRecords} - {self.totalAmount}'