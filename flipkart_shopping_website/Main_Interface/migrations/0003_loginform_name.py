# Generated by Django 4.1.2 on 2023-01-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Interface', '0002_alter_loginform_password_alter_loginform_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginform',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
