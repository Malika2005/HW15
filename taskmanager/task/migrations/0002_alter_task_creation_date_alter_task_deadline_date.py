# Generated by Django 4.2.6 on 2023-10-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline_date',
            field=models.DateField(),
        ),
    ]
