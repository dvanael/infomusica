# Generated by Django 5.0.1 on 2024-04-30 03:14

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=150, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(default=None, verbose_name='Conteúdo')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagem de Capa')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
