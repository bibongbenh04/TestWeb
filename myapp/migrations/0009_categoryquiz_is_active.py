# Generated by Django 4.1.7 on 2024-03-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryquiz',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
