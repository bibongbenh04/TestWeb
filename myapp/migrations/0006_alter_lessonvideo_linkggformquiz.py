# Generated by Django 4.1.7 on 2024-09-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_lessonvideo_linkggformquiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonvideo',
            name='linkggformquiz',
            field=models.URLField(null=True),
        ),
    ]
