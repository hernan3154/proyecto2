# Generated by Django 4.2.9 on 2024-03-22 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0015_rename_reset_token_user_password_reset_token_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password_reset_token',
            new_name='reset_password_token',
        ),
    ]
