# Generated by Django 5.1.1 on 2024-09-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
        ('doctors', '0009_doctoraffiliation'),
        ('patients', '0004_appointment_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='doctors',
            field=models.ManyToManyField(blank=True, to='doctors.doctor'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='patients',
            field=models.ManyToManyField(blank=True, related_name='clinics', to='patients.patient'),
        ),
    ]
