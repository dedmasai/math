# Generated by Django 4.2.7 on 2023-11-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_answerquiz_issubmitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isSubmitted',
            field=models.BooleanField(default=False),
        ),
    ]
