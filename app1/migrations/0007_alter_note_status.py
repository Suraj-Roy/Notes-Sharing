# Generated by Django 3.2 on 2021-08-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_signup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='status',
            field=models.CharField(default='pending', max_length=15),
        ),
    ]
