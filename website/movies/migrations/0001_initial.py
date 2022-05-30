# Generated by Django 4.0.1 on 2022-05-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Filmin Adı')),
                ('description', models.TextField(max_length=200, verbose_name='Film açıklaması')),
                ('image', models.CharField(max_length=100, verbose_name='Film kapağı')),
                ('created_date', models.DateField(verbose_name='oluşturulma tarihi')),
                ('Screening_date', models.CharField(max_length=20, verbose_name='Filmin Gösterime Giriş Tarihi')),
                ('director', models.CharField(max_length=30, verbose_name='yönetmen')),
                ('budget', models.CharField(max_length=20, verbose_name='Filmin bütçesi')),
                ('revenues', models.CharField(max_length=20, verbose_name='Filmin Hasılatı')),
                ('duration', models.CharField(max_length=20, verbose_name='Filmin Süresi')),
                ('movie_type', models.CharField(max_length=20, verbose_name='Filmin Türü')),
                ('IsPublished', models.BooleanField(default=True)),
            ],
        ),
    ]
