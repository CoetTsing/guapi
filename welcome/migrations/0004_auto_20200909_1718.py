# Generated by Django 3.0.8 on 2020-09-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_auto_20200909_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='profile',
            field=models.TextField(),
        ),
    ]
