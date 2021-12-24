# Generated by Django 4.0 on 2021-12-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
