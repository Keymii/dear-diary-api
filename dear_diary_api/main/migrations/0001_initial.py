# Generated by Django 4.1.7 on 2023-02-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userLogin',
            fields=[
                ('userid', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('pswd', models.CharField(max_length=30)),
            ],
        ),
    ]