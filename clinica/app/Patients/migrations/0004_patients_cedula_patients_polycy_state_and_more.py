# Generated by Django 5.1 on 2024-09-30 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0003_alter_patients_policy_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='policy_validity',
            field=models.DateField(default='0001-01-01', verbose_name='policy_validity'),
        ),
    ]
