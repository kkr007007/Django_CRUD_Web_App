# Generated by Django 5.1.7 on 2025-03-27 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_description', models.TextField()),
                ('image', models.ImageField(upload_to='recipe')),
            ],
        ),
    ]
