# Generated by Django 4.2.9 on 2024-04-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0030_rename_ntvg_notvg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notvg',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notvg/'),
        ),
    ]
