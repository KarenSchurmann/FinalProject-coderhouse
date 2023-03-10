# Generated by Django 4.1.4 on 2022-12-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collaborations', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MainTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='NewPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(default='', max_length=100)),
                ('main_theme', models.TextField()),
                ('authors', models.TextField()),
                ('published_date', models.DateField()),
                ('open_access', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(default='', max_length=100)),
                ('published_date', models.DateField()),
                ('open_access', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(default='', max_length=100)),
                ('main_theme', models.TextField()),
                ('authors', models.TextField()),
                ('published_date', models.DateField()),
                ('open_access', models.BooleanField()),
            ],
        ),
    ]
