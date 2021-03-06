# Generated by Django 4.0.3 on 2022-04-02 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=24)),
                ('courseDetails', models.CharField(max_length=150)),
                ('courseId', models.CharField(max_length=4)),
                ('courseTenure', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=24)),
                ('studentAddress', models.CharField(max_length=32)),
                ('birth_date', models.DateField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=14)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.course')),
            ],
        ),
    ]
