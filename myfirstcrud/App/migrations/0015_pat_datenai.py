# Generated by Django 4.2.1 on 2023-05-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_perso_salaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='pat',
            name='dateNai',
            field=models.DateField(default='1999-12-31'),
        ),
    ]
