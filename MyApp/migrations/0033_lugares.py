# Generated by Django 4.2.9 on 2024-04-20 22:25

import MyApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0032_alter_ciro_image_alter_divididos_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lugares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('hora', models.TimeField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=MyApp.models.image_upload_path)),
            ],
        ),
    ]
