# Generated by Django 3.0.5 on 2020-09-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0008_actor_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='short',
            field=models.TextField(default=''),
        ),
    ]