# Generated by Django 3.2.14 on 2022-08-06 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(max_length=255)),
                ('p_phone', models.IntegerField(max_length=10)),
                ('p_email', models.EmailField(max_length=254)),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctors')),
            ],
        ),
    ]
