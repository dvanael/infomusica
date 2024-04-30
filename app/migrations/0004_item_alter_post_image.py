# Generated by Django 5.0.1 on 2024-04-30 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, verbose_name='Nome')),
                ('description', models.TextField(default=None, max_length=550, verbose_name='Descrição')),
                ('image', models.ImageField(blank=True, null=True, upload_to='thumbnails/itens/', verbose_name='Imagem')),
                ('audio', models.FileField(blank=True, null=True, upload_to='documents/audio/', verbose_name='Amostra de Áudio')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='thumbnails/posts/', verbose_name='Imagem de Capa'),
        ),
    ]
