# Generated by Django 4.2.7 on 2023-11-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_task_touser_task_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='rightAnswCount',
        ),
        migrations.AddField(
            model_name='task',
            name='rightAnsw',
            field=models.BooleanField(default=False),
        ),
    ]
