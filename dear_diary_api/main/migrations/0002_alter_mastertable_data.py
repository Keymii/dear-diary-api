# Generated by Django 4.1.7 on 2023-02-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastertable',
            name='data',
            field=models.TextField(),
        ),
    ]
