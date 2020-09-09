# Generated by Django 3.0.5 on 2020-09-09 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0004_auto_20200909_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coworker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myID', models.CharField(max_length=10)),
                ('times', models.IntegerField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welcome.Actor')),
            ],
        ),
    ]
