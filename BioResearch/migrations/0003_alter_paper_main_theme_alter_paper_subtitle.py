# Generated by Django 4.1.4 on 2022-12-18 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioResearch', '0002_home_remove_maintheme_theme_author_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='main_theme',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paper',
            name='subtitle',
            field=models.CharField(max_length=100),
        ),
    ]