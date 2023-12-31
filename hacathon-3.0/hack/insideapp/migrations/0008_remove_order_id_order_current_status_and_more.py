# Generated by Django 4.1.3 on 2023-02-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insideapp', '0007_order_order_number_alter_useraccountregister_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='current_status',
            field=models.CharField(default=-1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('other', 'other'), ('Female', 'Female')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='State',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Punjab', 'Punjab'), ('West Benagal', 'West Bengal')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('kolkota', 'kolkota'), ('Patiala', 'Patiala')], default='patiala', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('other', 'other'), ('Female', 'Female')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='State',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Punjab', 'Punjab'), ('West Benagal', 'West Bengal')], default='Punjab', max_length=20),
        ),
        migrations.AlterField(
            model_name='workeraccountregister',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('kolkota', 'kolkota'), ('Patiala', 'Patiala')], default='patiala', max_length=20),
        ),
    ]
