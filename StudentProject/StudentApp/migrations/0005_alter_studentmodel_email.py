# Generated by Django 4.1.4 on 2023-01-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0004_rename_studentmodels_studentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
