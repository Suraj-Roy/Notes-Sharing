# Generated by Django 3.2 on 2021-08-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_signup_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='photo',
            field=models.ImageField(default='R.png', upload_to='profile'),
        ),
    ]
