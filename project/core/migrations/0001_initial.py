# Generated by Django 3.2.6 on 2021-08-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(unique=True)),
                ('url', models.URLField()),
                ('redirect_count', models.IntegerField()),
            ],
        ),
    ]
