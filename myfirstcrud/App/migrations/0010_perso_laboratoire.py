# Generated by Django 4.2.1 on 2023-05-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_labo_responsable'),
    ]

    operations = [
        migrations.AddField(
            model_name='perso',
            name='laboratoire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.labo'),
        ),
    ]
