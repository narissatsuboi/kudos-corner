# Generated by Django 3.2.5 on 2021-07-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kudos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sender', models.IntegerField(default=0)),
                ('recipient', models.IntegerField(default=0)),
                ('organisation', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('organisation', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=40)),
                ('ranking', models.IntegerField(default=0)),
                ('kudosSent', models.IntegerField(default=0)),
                ('starsReceived', models.IntegerField(default=0)),
                ('prizeCount', models.IntegerField(default=0)),
            ],
        ),
    ]
