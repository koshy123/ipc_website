# Generated by Django 4.1.5 on 2023-01-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contact',
            field=models.BooleanField(),
        ),
    ]
