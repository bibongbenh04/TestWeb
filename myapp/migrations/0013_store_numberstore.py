# Generated by Django 4.1.7 on 2024-03-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='numberStore',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]