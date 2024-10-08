# Generated by Django 5.1 on 2024-10-01 17:20

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employees', '0001_initial'),
        ('Patients', '0001_initial'),
        ('medicineInventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Description')),
                ('idEmployees', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Employees.employees')),
                ('idMedicineInventory', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='medicineInventory.medicineinventory')),
                ('idPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.patients')),
            ],
            options={
                'verbose_name': 'MedicalRecord',
                'verbose_name_plural': 'MedicalRecords',
            },
        ),
    ]
