# Generated by Django 4.2.5 on 2024-02-19 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
        ('General', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField(auto_now_add=True)),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField()),
                ('is_discharged', models.BooleanField(default=False)),
                ('bed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='General.bed')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.patient')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='General.room')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.ward')),
            ],
        ),
    ]
