# Generated by Django 3.2.15 on 2022-11-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_task_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]