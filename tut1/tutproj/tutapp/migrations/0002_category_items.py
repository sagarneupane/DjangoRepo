# Generated by Django 4.0.3 on 2022-04-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='items/')),
            ],
        ),
    ]
