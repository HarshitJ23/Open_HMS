# Generated by Django 3.0.5 on 2022-01-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20220114_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patientprescriptiondetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
