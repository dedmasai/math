# Generated by Django 4.2.7 on 2023-11-26 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_alter_task_touser_alter_task_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerquiz',
            name='taskID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.task'),
        ),
    ]
