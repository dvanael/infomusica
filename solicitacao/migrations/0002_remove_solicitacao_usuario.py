# Generated by Django 4.2.4 on 2023-09-30 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacao',
            name='usuario',
        ),
    ]
