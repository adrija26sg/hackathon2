# Generated by Django 4.1.3 on 2023-02-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insideapp', '0014_alter_useraccountregister_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccountregister',
            name='id',
        ),
        migrations.RemoveField(
            model_name='workeraccountregister',
            name='worker_id',
        ),
        migrations.AddField(
            model_name='useraccountregister',
            name='worker_id',
            field=models.AutoField(default=-1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workeraccountregister',
            name='id',
            field=models.BigAutoField(auto_created=True, default=-1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'other')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='State',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('West Benagal', 'West Bengal'), ('Delhi', 'Delhi')], default='Punjab', max_length=20),
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
            name='State',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('West Benagal', 'West Bengal'), ('Delhi', 'Delhi')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('kolkota', 'kolkota'), ('Patiala', 'Patiala')], default='patiala', max_length=20),
        ),
    ]
