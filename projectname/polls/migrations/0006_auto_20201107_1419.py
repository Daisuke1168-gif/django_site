# Generated by Django 3.1 on 2020-11-07 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_result2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result2',
            name='your_point',
        ),
        migrations.AddField(
            model_name='choice',
            name='your_point',
            field=models.IntegerField(default=0),
        ),
    ]