# Generated by Django 5.1 on 2024-09-28 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100, verbose_name='Nombres')),
                ('lastName', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo electrónico')),
                ('phone', models.CharField(max_length=10, verbose_name='Celular')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('rol', models.CharField(choices=[('MED', 'Medico(a)'), ('ENF', 'Enfermero(a)'), ('ADM', 'Administrativo'), ('LIM', 'Limpieza'), ('REG', 'Regente de farmacia'), ('FIS', 'Fisioterapeuta'), ('OTR', 'Otros')], default='OTR', max_length=50, verbose_name='Cargo')),
                ('username', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'Employees',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
