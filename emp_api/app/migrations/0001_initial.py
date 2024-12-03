# Generated by Django 5.1.3 on 2024-12-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.TextField()),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('position', models.TextField()),
                ('salary', models.IntegerField()),
                ('experiance', models.IntegerField()),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
