# Generated by Django 4.1.3 on 2023-02-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insideapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='State',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Delhi', 'Delhi'), ('West Benagal', 'West Bengal')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Patiala', 'Patiala'), ('kolkota', 'kolkota')], default='patiala', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='State',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Delhi', 'Delhi'), ('West Benagal', 'West Bengal')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Patiala', 'Patiala'), ('kolkota', 'kolkota')], default='patiala', max_length=20),
        ),
    ]
