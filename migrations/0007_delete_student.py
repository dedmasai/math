# Generated by Django 4.2.7 on 2023-11-25 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_vclass_work_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
