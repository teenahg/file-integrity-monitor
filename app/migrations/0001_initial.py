# Generated by Django 2.2.10 on 2021-06-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('location', models.CharField(max_length=350)),
                ('hash_value', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
