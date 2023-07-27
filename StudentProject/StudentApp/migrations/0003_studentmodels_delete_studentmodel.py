# Generated by Django 4.1.4 on 2023-01-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_remove_studentmodel_id_alter_studentmodel_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('student_image', models.ImageField(blank=True, upload_to='Student_Image/')),
                ('course', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('hobbies', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=100)),
                ('known_language', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('why_you_want', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentModel',
        ),
    ]