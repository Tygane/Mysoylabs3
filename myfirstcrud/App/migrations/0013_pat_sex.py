# Generated by Django 4.2.1 on 2023-05-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_remove_pat_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='pat',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
