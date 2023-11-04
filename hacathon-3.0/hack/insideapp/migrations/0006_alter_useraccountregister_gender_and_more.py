# Generated by Django 4.1.3 on 2023-02-25 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insideapp', '0005_alter_useraccountregister_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('kolkota', 'kolkota'), ('Patiala', 'Patiala')], default='patiala', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('kolkota', 'kolkota'), ('Patiala', 'Patiala')], default='patiala', max_length=20),
        ),
    ]
