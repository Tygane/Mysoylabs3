# Generated by Django 4.2.1 on 2023-05-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_labo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='labo',
            name='domaine',
            field=models.CharField(default='_', max_length=40),
        ),
    ]