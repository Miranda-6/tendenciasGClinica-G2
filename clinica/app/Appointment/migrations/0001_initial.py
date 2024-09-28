# Generated by Django 5.1 on 2024-09-28 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employees', '0001_initial'),
        ('Patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('reason', models.CharField(blank=True, max_length=100, verbose_name='Reason')),
                ('status', models.CharField(choices=[('PROGR', 'Programada'), ('COMPL', 'Completada'), ('CANCEL', 'Cancelada')], default='PROGR', max_length=20, verbose_name='Status')),
                ('idEmployee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employees')),
                ('idPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.patients')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]
