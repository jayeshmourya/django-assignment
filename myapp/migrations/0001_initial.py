# Generated by Django 4.2 on 2023-04-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
    ]
