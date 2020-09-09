# Generated by Django 3.0.8 on 2020-09-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myID', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=3000)),
                ('profile', models.CharField(max_length=3000)),
                ('jpg', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myID', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('directors', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=600)),
                ('actorsShort', models.CharField(max_length=5000)),
                ('profile', models.CharField(max_length=5000)),
                ('rating', models.CharField(max_length=5)),
                ('comments', models.CharField(max_length=5000)),
                ('actors', models.ManyToManyField(to='welcome.Actor')),
            ],
        ),
    ]