# Generated by Django 3.2 on 2021-08-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_note_uploadingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='uploadingdate',
            field=models.DateTimeField(),
        ),
    ]