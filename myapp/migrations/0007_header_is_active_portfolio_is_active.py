# Generated by Django 4.1.7 on 2024-03-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_portfolio_rename_subtitle_header_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
