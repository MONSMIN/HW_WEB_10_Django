# Generated by Django 4.2.4 on 2023-08-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(default='Default description'),
        ),
    ]
