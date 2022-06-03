# Generated by Django 4.0.5 on 2022-06-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('createdAt', models.DateTimeField()),
            ],
        ),
    ]