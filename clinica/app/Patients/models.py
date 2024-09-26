from django.db import models

class Patients(models.Model):
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEM = "F", "Female"
        OTHER = "O", "Other"


    firstName = models.CharField('First Name', max_length=100)
    lastName = models.CharField('Last name', max_length=100)
    email = models.CharField('Email', max_length=100)
    phone = models.CharField('Phone', max_length=10)
    birthDate = models.DateField('Birth Date', blank=False, null=False)
    address = models.CharField('Address', max_length=50)
    gender = models.CharField(
        'Gender',
        max_length=2,
        choices=Gender.choices,
        default=Gender.MALE
    )
    emergency_contact = models.CharField('Emergency Contact', max_length=20)
    insurance_entity = models.CharField("Insurance", max_length=50)
    
    #I think we dont need to assign usernames and passwords to Patients, they won't be the
    #won't do login into de app

    #username = models.CharField('User', max_length=100)
    #password = models.CharField('Psaasword', max_length=100)
    
    def __str__(self):
        return f'{self.firstName} - {self.email} - {self.phone}'