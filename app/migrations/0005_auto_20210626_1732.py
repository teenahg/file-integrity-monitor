# Generated by Django 2.2.10 on 2021-06-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210626_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
