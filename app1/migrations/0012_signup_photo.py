# Generated by Django 3.2 on 2021-08-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20210829_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
