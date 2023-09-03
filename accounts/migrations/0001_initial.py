# Generated by Django 4.2.4 on 2023-09-02 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHospitalManagement',
            fields=[
                ('account_type', models.CharField(choices=[('Doctor', 'Doctor'), ('Patient', 'Patient'), ('Admin', 'Admin'), ('User', 'User'), ('Technologist', 'Technologist'), ('Recieptionist', 'Recietionist'), ('Accounce', 'Accounce'), ('Cash', 'Cash')], max_length=20)),
                ('employee_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(blank=True, max_length=1000, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.IntegerField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]